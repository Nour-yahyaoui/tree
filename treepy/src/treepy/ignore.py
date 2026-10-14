"""``.gitignore`` flavoured pattern matching.

Only the subset a tree printer needs is implemented: comments and blank lines,
``!`` negation, a trailing ``/`` to match directories only, a leading ``/``
for patterns anchored at the scan root, and the ``*``, ``?`` and ``**`` globs.
Patterns are matched against paths relative to the root of the scan.
"""

from __future__ import annotations

import os
import re
from dataclasses import dataclass, field
from typing import Iterable, List, Optional

from .node import Node, Stats

__all__ = ["IgnoreSet", "Pattern", "filter_tree", "prune_tree"]


def _translate(pattern: str) -> str:
    """Translate one gitignore glob into the body of a regular expression."""
    parts: List[str] = []
    index = 0
    length = len(pattern)
    while index < length:
        char = pattern[index]
        if char == "*":
            if pattern[index : index + 2] == "**":
                index += 2
                if pattern[index : index + 1] == "/":
                    index += 1
                    parts.append("(?:.*/)?")
                else:
                    parts.append(".*")
                continue
            parts.append("[^/]*")
        elif char == "?":
            parts.append("[^/]")
        elif char == "[":
            closing = pattern.find("]", index + 1)
            if closing == -1:
                parts.append(re.escape(char))
            else:
                body = pattern[index + 1 : closing]
                if body.startswith("!"):
                    body = "^" + body[1:]
                parts.append("[" + body + "]")
                index = closing + 1
                continue
        else:
            parts.append(re.escape(char))
        index += 1
    return "".join(parts)


@dataclass
class Pattern:
    """A single compiled gitignore-style pattern."""

    raw: str
    negated: bool
    dir_only: bool
    anchored: bool
    regex: "re.Pattern[str]"

    @classmethod
    def parse(cls, line: str) -> Optional["Pattern"]:
        text = line.rstrip("\n").strip()
        if not text or text.startswith("#"):
            return None
        negated = text.startswith("!")
        if negated:
            text = text[1:].strip()
        dir_only = text.endswith("/")
        if dir_only:
            text = text[:-1]
        anchored = text.startswith("/") or "/" in text
        text = text.lstrip("/")
        if not text:
            return None
        return cls(
            raw=line.rstrip("\n"),
            negated=negated,
            dir_only=dir_only,
            anchored=anchored,
            regex=re.compile(_translate(text)),
        )

    def matches(self, relative_path: str, is_dir: bool) -> bool:
        """True when this pattern covers the given relative path."""
        if self.dir_only and not is_dir:
            return False
        relative_path = relative_path.replace(os.sep, "/").strip("/")
        if not relative_path:
            return False
        if self.anchored:
            return self.regex.fullmatch(relative_path) is not None
        parts = relative_path.split("/")
        for start in range(len(parts)):
            if self.regex.fullmatch("/".join(parts[start:])) is not None:
                return True
        return False


@dataclass
class IgnoreSet:
    """An ordered list of patterns; later patterns win, as in git."""

    patterns: List[Pattern] = field(default_factory=list)

    def __bool__(self) -> bool:
        return bool(self.patterns)

    def __len__(self) -> int:
        return len(self.patterns)

    @classmethod
    def from_lines(cls, lines: Iterable[str]) -> "IgnoreSet":
        parsed = [pattern for pattern in (Pattern.parse(line) for line in lines) if pattern]
        return cls(parsed)

    @classmethod
    def from_patterns(cls, patterns: Iterable[str]) -> "IgnoreSet":
        """Build a set from command line style globs such as ``*.log``."""
        parsed = [pattern for pattern in (Pattern.parse(item) for item in patterns) if pattern]
        return cls(parsed)

    @classmethod
    def from_file(cls, path: str) -> "IgnoreSet":
        """Read *path* if it exists; a missing ignore file is not an error."""
        if not os.path.isfile(path):
            return cls()
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            return cls.from_lines(handle)

    def matches(self, relative_path: str, is_dir: bool) -> bool:
        ignored = False
        for pattern in self.patterns:
            if pattern.matches(relative_path, is_dir):
                ignored = not pattern.negated
        return ignored

    def merge(self, other: "IgnoreSet") -> "IgnoreSet":
        return IgnoreSet(self.patterns + other.patterns)


def filter_tree(node: Node, include: Pattern, stats: Optional[Stats] = None) -> Optional[Node]:
    """Keep only the entries matching *include*, pruning empty directories.

    Directories survive when at least one descendant survives, so the shape of
    the path is preserved.  Passing *stats* keeps the summary counters honest
    for the entries that were dropped.
    """
    if not node.is_dir:
        if include.matches(node.relative or node.name, False):
            return node
        if stats is not None:
            _subtract_tree(node, stats)
        return None

    kept = []
    for child in node.children:
        survivor = filter_tree(child, include, stats)
        if survivor is not None:
            kept.append(survivor)
    node.children = kept
    if not kept and node.relative:
        if stats is not None:
            _subtract_tree(node, stats)
        return None
    return node


def _subtract_tree(node: Node, stats: Stats) -> None:
    """Undo the walker's counters for a discarded subtree."""
    for item in node.walk():
        if item.is_dir:
            stats.dirs -= 1
        elif not item.error:
            # A failed stat produces an error node, not a counted file.
            stats.files -= 1
            stats.total_bytes -= item.size
        if item.symlink:
            stats.symlinks -= 1
        if item.error:
            stats.errors -= 1


def prune_tree(node: Node, max_entries: int, stats: Optional[Stats] = None) -> Node:
    """Trim wide directories, updating *stats* for every discarded entry."""
    if max_entries < 1:
        raise ValueError("max_entries must be at least 1")
    if stats is not None:
        for child in node.children[max_entries:]:
            _subtract_tree(child, stats)
    node.children = node.children[:max_entries]
    for child in node.children:
        if child.is_dir:
            prune_tree(child, max_entries, stats)
    return node
