"""The command line: argparse, one function per command, no surprises."""

from __future__ import annotations

import argparse
import sqlite3
import sys
from typing import List, Optional, TextIO

from .models import InvalidLink
from .store import Shelf

DEFAULT_DB = "~/.raf/shelf.db"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="raf", description="a read-later shelf you host yourself")
    parser.add_argument("--db", default=DEFAULT_DB, help="the shelf file (default: ~/.raf/shelf.db)")
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="save a url")
    add.add_argument("url")
    add.add_argument("--title", default="")
    add.add_argument("--tag", action="append", default=[])
    add.add_argument("--note", default="")

    for name, help_text in (("list", "the shelf"), ("unread", "what is still unread")):
        listing = commands.add_parser(name, help=help_text)
        listing.add_argument("--tag", default=None)
        listing.add_argument("--limit", type=int, default=0)

    show = commands.add_parser("show", help="one link, with its note")
    show.add_argument("id", type=int)

    for name in ("read", "unread-one"):
        mark = commands.add_parser(name, help="mark a link read" if name == "read" else "mark a link unread")
        mark.add_argument("id", type=int)

    tag = commands.add_parser("tag", help="add tags")
    tag.add_argument("id", type=int)
    tag.add_argument("tags", nargs="+")

    untag = commands.add_parser("untag", help="remove tags")
    untag.add_argument("id", type=int)
    untag.add_argument("tags", nargs="+")

    rm = commands.add_parser("rm", help="forget a link")
    rm.add_argument("id", type=int)

    search = commands.add_parser("search", help="words, tag:name, is:unread")
    search.add_argument("query", nargs="+")

    commands.add_parser("tags", help="every tag and how often it is used")
    commands.add_parser("stats", help="the numbers")

    export = commands.add_parser("export", help="write the shelf out as json")
    export.add_argument("--out", default=None)
    import_ = commands.add_parser("import", help="read a shelf export back in")
    import_.add_argument("file")

    return parser


def main(argv: Optional[List[str]] = None, out: Optional[TextIO] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if getattr(args, "limit", 0) < 0:
        parser.error("--limit must be zero or greater")
    out = out or sys.stdout
    shelf = None

    try:
        shelf = Shelf(args.db)
        return dispatch(shelf, args, out)
    except (InvalidLink, OSError, sqlite3.Error) as error:
        print(str(error), file=out)
        return 1
    finally:
        if shelf is not None:
            shelf.close()


def dispatch(shelf: Shelf, args, out: TextIO) -> int:
    command = args.command

    if command == "add":
        link = shelf.add(args.url, title=args.title, tags=args.tag, note=args.note)
        print(f"{link.id}  {link.title or link.url}", file=out)
        return 0

    if command in ("list", "unread"):
        links = shelf.links(tag=args.tag, unread_only=command == "unread")
        if args.limit:
            links = links[: args.limit]
        for link in links:
            print(f"{link.id:4}  {link}", file=out)
        print(f"{len(links)} link(s)", file=out)
        return 0

    if command == "show":
        link = shelf.get(args.id)
        if link is None:
            print(f"no link {args.id}", file=out)
            return 1
        print(link.url, file=out)
        print(link.title or "(no title)", file=out)
        if link.tags:
            print("tags: " + ", ".join(link.tags), file=out)
        if link.note:
            print(link.note, file=out)
        return 0

    if command in ("read", "unread-one"):
        if shelf.mark(args.id, read=command == "read"):
            return 0
        print(f"no link {args.id}", file=out)
        return 1

    if command in ("tag", "untag") and shelf.get(args.id) is None:
        print(f"no link {args.id}", file=out)
        return 1

    if command == "tag":
        print(f"{shelf.tag(args.id, ' '.join(args.tags))} tag(s) added", file=out)
        return 0

    if command == "untag":
        print(f"{shelf.untag(args.id, ' '.join(args.tags))} tag(s) removed", file=out)
        return 0

    if command == "rm":
        if shelf.remove(args.id):
            return 0
        print(f"no link {args.id}", file=out)
        return 1

    if command == "search":
        for link in shelf.search(" ".join(args.query)):
            print(f"{link.id:4}  {link}", file=out)
        return 0

    if command == "tags":
        for tag, count in shelf.tags():
            print(f"{tag:20} {count}", file=out)
        return 0

    if command == "stats":
        stats = shelf.stats()
        for key in ("total", "read", "unread", "tags", "hosts"):
            print(f"{key:8} {stats[key]}", file=out)
        return 0

    if command == "export":
        payload = shelf.export()
        if args.out:
            with open(args.out, "w", encoding="utf-8") as handle:
                handle.write(payload)
            print(f"wrote {args.out}", file=out)
        else:
            print(payload, file=out, end="")
        return 0

    if command == "import":
        with open(args.file, encoding="utf-8") as handle:
            try:
                added, skipped = shelf.import_(handle.read())
            except InvalidLink as error:
                print(str(error), file=out)
                return 1
        print(f"{added} added, {skipped} skipped", file=out)
        return 0

    raise SystemExit(f"unknown command: {command}")  # pragma: no cover - argparse guards this


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
