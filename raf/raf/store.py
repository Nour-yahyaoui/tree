"""The shelf: one sqlite file, a schema that upgrades itself, and no ORM."""

from __future__ import annotations

import json
import os
import sqlite3
from typing import Iterable, List, Optional, Sequence
from urllib.parse import urlparse

from .models import Link, InvalidLink, normalise_url, now, parse_tags
from .search import run

SCHEMA_VERSION = 2

SCHEMA = """
CREATE TABLE IF NOT EXISTS links (
    id    INTEGER PRIMARY KEY,
    url   TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL DEFAULT '',
    note  TEXT NOT NULL DEFAULT '',
    added TEXT NOT NULL,
    read  INTEGER NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS tags (
    link_id INTEGER NOT NULL REFERENCES links(id) ON DELETE CASCADE,
    tag     TEXT NOT NULL,
    PRIMARY KEY (link_id, tag)
);
CREATE INDEX IF NOT EXISTS links_added ON links (added);
CREATE INDEX IF NOT EXISTS tags_tag ON tags (tag);
"""


class Shelf:
    def __init__(self, path: str = ":memory:"):
        if path != ":memory:":
            path = os.path.expanduser(path)
            directory = os.path.dirname(os.path.abspath(path))
            os.makedirs(directory, exist_ok=True)
        self.path = path
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self.db.execute("PRAGMA foreign_keys = ON")
        self.migrate()

    def migrate(self) -> None:
        """`PRAGMA user_version` is the schema version. Version 0 knew no tags."""
        self.db.executescript(SCHEMA)
        version = self.db.execute("PRAGMA user_version").fetchone()[0]
        if version < 1:
            self.db.execute("UPDATE links SET read = 0 WHERE read IS NULL")
        self.db.execute(f"PRAGMA user_version = {SCHEMA_VERSION}")
        self.db.commit()

    def close(self) -> None:
        self.db.close()

    # writing ---------------------------------------------------------------

    def add(self, url: str, title: str = "", tags: str | Sequence[str] = (), note: str = "") -> Link:
        normalised = normalise_url(url)
        tag_list = parse_tags(tags) if isinstance(tags, str) else parse_tags(" ".join(tags))
        cursor = self.db.execute(
            "INSERT OR IGNORE INTO links (url, title, note, added) VALUES (?, ?, ?, ?)",
            (normalised, title.strip(), note.strip(), now()),
        )
        if cursor.rowcount == 0:
            link = self._one(url=normalised)
            if link is None:  # pragma: no cover - only if the row vanished
                raise RuntimeError("the link disappeared between two statements")
            return link
        link_id = cursor.lastrowid
        for tag in tag_list:
            self.db.execute("INSERT OR IGNORE INTO tags (link_id, tag) VALUES (?, ?)", (link_id, tag))
        self.db.commit()
        return self._one(link_id)

    def mark(self, link_id: int, read: bool = True) -> bool:
        """True when the link is there and is now in the state you asked for."""
        cursor = self.db.execute("UPDATE links SET read = ? WHERE id = ?", (1 if read else 0, link_id))
        self.db.commit()
        if cursor.rowcount == 0:
            return False
        row = self.db.execute("SELECT read FROM links WHERE id = ?", (link_id,)).fetchone()
        return bool(row[0]) == read

    def tag(self, link_id: int, tags: str) -> int:
        added = 0
        for tag in parse_tags(tags):
            cursor = self.db.execute("INSERT OR IGNORE INTO tags (link_id, tag) VALUES (?, ?)", (link_id, tag))
            added += cursor.rowcount
        self.db.commit()
        return added

    def untag(self, link_id: int, tags: str) -> int:
        removed = 0
        for tag in parse_tags(tags):
            cursor = self.db.execute("DELETE FROM tags WHERE link_id = ? AND tag = ?", (link_id, tag))
            removed += cursor.rowcount
        self.db.commit()
        return removed

    def remove(self, link_id: int) -> bool:
        cursor = self.db.execute("DELETE FROM links WHERE id = ?", (link_id,))
        self.db.commit()
        return cursor.rowcount > 0

    # reading ---------------------------------------------------------------

    def _one(self, link_id: int | None = None, url: str | None = None) -> Optional[Link]:
        if link_id is not None:
            row = self.db.execute("SELECT * FROM links WHERE id = ?", (link_id,)).fetchone()
        else:
            row = self.db.execute("SELECT * FROM links WHERE url = ?", (url,)).fetchone()
        return self._link(row) if row else None

    def _link(self, row) -> Link:
        tags = self.db.execute(
            "SELECT tag FROM tags WHERE link_id = ? ORDER BY tag", (row["id"],)
        ).fetchall()
        return Link(
            id=row["id"], url=row["url"], title=row["title"], note=row["note"],
            added=row["added"], read=bool(row["read"]),
            tags=tuple(tag["tag"] for tag in tags),
        )

    def links(self, tag: str | None = None, unread_only: bool = False) -> List[Link]:
        sql = "SELECT * FROM links"
        where, params = [], []
        if unread_only:
            where.append("read = 0")
        if tag:
            where.append("id IN (SELECT link_id FROM tags WHERE tag = ?)")
            params.append(tag.lower())
        if where:
            sql += " WHERE " + " AND ".join(where)
        sql += " ORDER BY added DESC, id DESC"
        return [self._link(row) for row in self.db.execute(sql, params)]

    def get(self, link_id: int) -> Optional[Link]:
        return self._one(link_id)

    def search(self, text: str) -> List[Link]:
        return [link for _, link in run(self.links(), text)]

    def tags(self) -> List[tuple]:
        return [
            (row["tag"], row["count"])
            for row in self.db.execute(
                "SELECT tag, COUNT(*) AS count FROM tags GROUP BY tag ORDER BY count DESC, tag"
            )
        ]

    def stats(self) -> dict:
        row = self.db.execute(
            "SELECT COUNT(*) AS total, SUM(read) AS read FROM links"
        ).fetchone()
        total = row["total"] or 0
        read = row["read"] or 0
        return {
            "total": total,
            "read": read,
            "unread": total - read,
            "tags": len(self.tags()),
            "hosts": len({urlparse(row["url"]).hostname for row in self.db.execute("SELECT url FROM links")}),
        }

    # moving data -----------------------------------------------------------

    def export(self) -> str:
        payload = {
            "version": SCHEMA_VERSION,
            "links": [
                {
                    "url": link.url,
                    "title": link.title,
                    "tags": list(link.tags),
                    "note": link.note,
                    "read": link.read,
                    "added": link.added,
                }
                for link in self.links()
            ],
        }
        return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"

    def import_(self, text: str) -> tuple:
        """Returns (added, skipped). Anything the file has that we cannot read
        is skipped rather than guessed at."""
        try:
            payload = json.loads(text)
        except ValueError as error:
            raise InvalidLink(f"not a shelf export: {error}") from error
        if not isinstance(payload, dict) or not isinstance(payload.get("links"), list):
            raise InvalidLink("not a shelf export: no links")
        added = skipped = 0
        for item in payload["links"]:
            try:
                if not isinstance(item, dict):
                    raise InvalidLink("not a link object")
                if any(not isinstance(item.get(key, ""), str) for key in ("title", "note", "added")):
                    raise InvalidLink("invalid link text")
                tags = item.get("tags", ())
                if not isinstance(tags, (str, list, tuple)) or (
                    not isinstance(tags, str) and any(not isinstance(tag, str) for tag in tags)
                ):
                    raise InvalidLink("invalid tags")
                if not isinstance(item.get("read", False), bool):
                    raise InvalidLink("invalid read flag")
                normalised = normalise_url(item["url"])
                if self._one(url=normalised) is not None:
                    skipped += 1
                    continue
                link = self.add(
                    normalised,
                    title=item.get("title", ""),
                    tags=item.get("tags", ()),
                    note=item.get("note", ""),
                )
                if item.get("read"):
                    self.mark(link.id, True)
                if item.get("added"):
                    # an import restores the date the link was saved, not the date
                    # of the import
                    self.db.execute("UPDATE links SET added = ? WHERE id = ?", (str(item["added"]), link.id))
                    self.db.commit()
                added += 1
            except (KeyError, TypeError, InvalidLink):
                skipped += 1
        return added, skipped
