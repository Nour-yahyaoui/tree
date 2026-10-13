"""The command line interface.

``main`` is the only public function here; it parses arguments, walks the
requested paths and writes the result.  Keeping the parser in its own
function makes it easy to test option handling without touching the disk.
"""

from __future__ import annotations

import argparse
import sys
from typing import List, Optional, Sequence

from . import __version__
from .ignore import IgnoreSet, Pattern, filter_tree, prune_tree
from .node import Node, Stats
from .render import RenderOptions, render_json, render_text
from .style import build_style, plain_style
from .walker import WalkOptions, default_error_hook, walk

__all__ = ["build_parser", "main"]

PROGRAM = "treepy"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog=PROGRAM,
        description="Print a directory tree, in colour or as JSON.",
        epilog="Run 'treepy .' to print the current directory.",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=["."],
        help="one or more directories to print (default: the current one)",
    )
    parser.add_argument("--version", action="version", version=f"{PROGRAM} {__version__}")

    limits = parser.add_argument_group("what to show")
    limits.add_argument("-L", "--depth", type=int, metavar="N", help="descend at most N levels")
    limits.add_argument("-a", "--all", action="store_true", help="include hidden entries")
    limits.add_argument("-d", "--dirs-only", action="store_true", help="list directories only")
    limits.add_argument("-l", "--follow-links", action="store_true", help="follow symbolic links")
    limits.add_argument(
        "-I",
        "--exclude",
        action="append",
        metavar="PATTERN",
        help="skip entries matching PATTERN (repeatable)",
    )
    limits.add_argument(
        "-P",
        "--include",
        metavar="PATTERN",
        help="show only entries matching PATTERN",
    )
    limits.add_argument(
        "--gitignore",
        action="store_true",
        help="respect the .gitignore file found in each root",
    )
    limits.add_argument("--prune", action="store_true", help="hide directories with no children")
    limits.add_argument(
        "--max-entries",
        type=int,
        metavar="N",
        help="keep at most N children per directory",
    )

    order = parser.add_argument_group("ordering")
    order.add_argument(
        "--sort",
        choices=("name", "size", "mtime", "none"),
        default="name",
        help="sort key for entries (default: name)",
    )
    order.add_argument("-r", "--reverse", action="store_true", help="reverse the sort order")

    output = parser.add_argument_group("output")
    output.add_argument("-s", "--size", action="store_true", help="show entry sizes")
    output.add_argument(
        "-H", "--human-readable", action="store_true", help="show sizes in KiB, MiB, ..."
    )
    output.add_argument("--du", action="store_true", help="show directory totals instead of sizes")
    output.add_argument("--json", action="store_true", help="emit JSON instead of text")
    output.add_argument("--ascii", action="store_true", help="use ASCII line drawing characters")
    output.add_argument(
        "--color",
        choices=("auto", "always", "never"),
        default="auto",
        help="when to colourise the output (default: auto)",
    )
    output.add_argument("-q", "--quiet", action="store_true", help="hide the summary line")
    output.add_argument("-o", "--output", metavar="FILE", help="write to FILE instead of stdout")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.depth is not None and args.depth < 0:
        parser.error("--depth must be zero or greater")
    if args.max_entries is not None and args.max_entries < 1:
        parser.error("--max-entries must be at least 1")

    ignore = _build_ignore(args)
    options = WalkOptions(
        max_depth=args.depth,
        show_hidden=args.all,
        dirs_only=args.dirs_only,
        follow_symlinks=args.follow_links,
        sort_key=args.sort,
        reverse=args.reverse,
        prune_empty=args.prune,
        ignore=ignore,
        error_hook=default_error_hook,
    )

    stats = Stats()
    roots: List[Node] = []
    for path in args.paths:
        roots.append(walk(path, options, stats))

    scan_errors = stats.errors

    if args.include:
        pattern = Pattern.parse(args.include)
        if pattern is None:
            parser.error("--include needs a non-empty pattern")
        filtered: List[Node] = []
        for root in roots:
            survivor = filter_tree(root, pattern, stats)
            if survivor is not None:
                filtered.append(survivor)
        roots = filtered

    if args.max_entries is not None:
        for root in roots:
            prune_tree(root, args.max_entries, stats)

    options_render = RenderOptions(
        show_sizes=args.size or args.du,
        human=args.human_readable,
        dir_sizes=args.du,
        ascii_only=args.ascii,
        show_summary=not args.quiet,
        show_bytes_total=args.size or args.du,
        style=plain_style() if args.json else build_style(args.color),
    )

    if args.json:
        document = render_json(roots, stats, options_render)
    else:
        blocks = [render_text(root, options_render) for root in roots]
        document = "\n\n".join(blocks) + "\n"

    _emit(document, args.output)
    return 1 if scan_errors else 0


def _build_ignore(args: argparse.Namespace) -> Optional[IgnoreSet]:
    """Combine --exclude and --gitignore into a single matcher."""
    combined: Optional[IgnoreSet] = None
    if args.exclude:
        combined = IgnoreSet.from_patterns(args.exclude)
    if args.gitignore:
        for path in args.paths:
            candidate = f"{path.rstrip('/')}/.gitignore" if path != "." else ".gitignore"
            found = IgnoreSet.from_file(candidate)
            if found:
                combined = found if combined is None else combined.merge(found)
    return combined


def _emit(document: str, destination: Optional[str]) -> None:
    if destination:
        with open(destination, "w", encoding="utf-8") as handle:
            handle.write(document)
        return
    sys.stdout.write(document)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
