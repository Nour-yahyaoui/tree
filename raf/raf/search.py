"""The search query language, and the ranking.

A query is words, plus two filters: `tag:name` and `is:unread` (or `is:read`).
Ranking is a weighted sum, and a title hit counts for more than a note hit,
because that is how people look for the thing they saved.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, List, Sequence, Tuple


@dataclass
class Query:
    words: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    read: bool | None = None

    def __bool__(self) -> bool:
        return bool(self.words or self.tags or self.read is not None)


def parse_query(text: str) -> Query:
    query = Query()
    for piece in (text or "").split():
        lowered = piece.lower()
        if lowered.startswith("tag:") and lowered[4:].strip():
            query.tags.append(lowered[4:].strip())
        elif lowered.startswith("is:") and lowered[3:].strip() in ("read", "unread"):
            query.read = lowered[3:].strip() == "read"
        else:
            # an unknown filter is just a word: searching for it is better than
            # silently dropping what the person typed
            query.words.append(lowered)
    return query


WEIGHTS = (
    ("title", 4.0),
    ("tag", 3.0),
    ("url", 2.0),
    ("note", 1.0),
)


def score(link, query: Query) -> float:
    """Higher is better. A query that asks for a tag only ranks by how well
    the words match, so a filter never becomes a score all on its own."""
    if not query.words:
        return 1.0 if matches(link, query) else 0.0
    total = 0.0
    for word in query.words:
        for field_name, weight in WEIGHTS:
            value = {
                "title": link.title.lower(),
                "tag": " ".join(tag.lower() for tag in link.tags),
                "url": link.url.lower(),
                "note": link.note.lower(),
            }[field_name]
            if word in value:
                total += weight
    return total


def matches(link, query: Query) -> bool:
    if query.read is not None and bool(link.read) != query.read:
        return False
    for tag in query.tags:
        if tag not in {t.lower() for t in link.tags}:
            return False
    for word in query.words:
        haystack = " ".join([link.title, link.url, link.note, " ".join(link.tags)]).lower()
        if word not in haystack:
            return False
    return True


def run(links: Iterable, text: str) -> List[Tuple[float, object]]:
    """The links the query keeps, best first, and stable inside a score."""
    query = parse_query(text)
    kept = [(score(link, query), link) for link in links if matches(link, query)]
    kept.sort(key=lambda pair: pair[0], reverse=True)
    return kept
