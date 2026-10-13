"""Filesystem traversal.

The walker is the only module in treepy that touches the filesystem.  It
turns a path into a :class:`~treepy.node.Node` tree and refuses to get stuck:
symlink cycles are detected with the ``(st_dev, st_ino)`` pair of every
directory it descends into while ``follow_symlinks`` is on.
"""

from __future__ import annotations

import os
import stat as stat_module
from dataclasses import dataclass
from typing import Callable, List, Optional, Set, Tuple

from .ignore import IgnoreSet
from .node import Node, Stats

__all__ = ["WalkOptions", "walk", "SORT_KEYS"]

SORT_KEYS = ("name", "size", "mtime", "none")

ErrorHook = Callable[[str, OSError], None]
_Identity = Tuple[int, int]


def default_error_hook(path: str, error: OSError) -> None:
    """Print a single line to stderr, the way the C ``tree`` utility does."""
    import sys

    print(f"treepy: {path}: {error.strerror or error}", file=sys.stderr)


@dataclass
class WalkOptions:
    """Everything the walker needs to know about how to walk."""

    max_depth: Optional[int] = None
    show_hidden: bool = False
    dirs_only: bool = False
    follow_symlinks: bool = False
    sort_key: str = "name"
    reverse: bool = False
    prune_empty: bool = False
    ignore: Optional[IgnoreSet] = None
    error_hook: Optional[ErrorHook] = default_error_hook

    def __post_init__(self) -> None:
        if self.sort_key not in SORT_KEYS:
            allowed = ", ".join(SORT_KEYS)
            raise ValueError(f"unknown sort key {self.sort_key!r}, expected one of {allowed}")
        if self.max_depth is not None and self.max_depth < 0:
            raise ValueError("max_depth must be zero or greater")


def walk(
    root: str,
    options: Optional[WalkOptions] = None,
    stats: Optional[Stats] = None,
) -> Node:
    """Walk *root* and return it as a tree of :class:`Node` objects.

    *stats* is updated in place, so callers that print several roots can pass
    the same :class:`Stats` instance for every call and get a combined
    summary at the end.
    """
    options = options or WalkOptions()
    stats = stats if stats is not None else Stats()

    trimmed = root.rstrip(os.sep) or root
    try:
        info = os.stat(trimmed) if options.follow_symlinks else os.lstat(trimmed)
    except OSError as exc:
        _report(options, trimmed, exc)
        stats.errors += 1
        return Node(
            name=os.path.basename(trimmed) or trimmed,
            path=trimmed,
            is_dir=False,
            error=str(exc),
        )

    is_dir = stat_module.S_ISDIR(info.st_mode)
    is_link = os.path.islink(trimmed)
    node = Node(
        name=os.path.basename(trimmed) or trimmed,
        path=trimmed,
        is_dir=is_dir,
        size=0 if is_dir else info.st_size,
        mtime=info.st_mtime,
        symlink=is_link,
        link_target=_read_link(trimmed) if is_link else None,
    )
    if is_link:
        stats.symlinks += 1
    if is_dir:
        stats.dirs += 1
        seen: Set[_Identity] = {_identity(info)} if options.follow_symlinks else set()
        if options.max_depth is None or options.max_depth >= 1:
            _fill(node, options, stats, seen, depth=1)
    else:
        stats.files += 1
        stats.total_bytes += node.size
    return node


def _fill(
    node: Node,
    options: WalkOptions,
    stats: Stats,
    seen: Set[_Identity],
    depth: int,
) -> None:
    """Read one directory and attach its surviving entries to *node*."""
    try:
        entries = list(os.scandir(node.path))
    except OSError as exc:
        node.error = str(exc)
        stats.errors += 1
        _report(options, node.path, exc)
        return

    for entry in _sorted(entries, options):
        relative = f"{node.relative}/{entry.name}" if node.relative else entry.name
        if not _keep(entry, relative, options):
            continue
        child = _visit(entry, relative, options, stats, seen, depth)
        if child is None:
            continue
        if options.prune_empty and child.is_dir and not child.children and not child.error:
            stats.dirs -= 1  # the directory was counted, then dropped
            continue
        node.add(child)


def _visit(
    entry: "os.DirEntry[str]",
    relative: str,
    options: WalkOptions,
    stats: Stats,
    seen: Set[_Identity],
    depth: int,
) -> Optional[Node]:
    """Turn a single directory entry into a node, recursing for directories."""
    trace = options.follow_symlinks
    try:
        info = entry.stat(follow_symlinks=trace)
    except OSError as exc:
        stats.errors += 1
        _report(options, entry.path, exc)
        return Node(
            name=entry.name,
            path=entry.path,
            is_dir=False,
            relative=relative,
            error=str(exc),
        )

    is_link = entry.is_symlink()
    is_dir = stat_module.S_ISDIR(info.st_mode)
    node = Node(
        name=entry.name,
        path=entry.path,
        is_dir=is_dir,
        size=0 if is_dir else info.st_size,
        mtime=info.st_mtime,
        relative=relative,
        symlink=is_link,
        link_target=_read_link(entry.path) if is_link else None,
    )

    if is_link:
        stats.symlinks += 1
    if not is_dir:
        stats.files += 1
        stats.total_bytes += node.size
        return node

    stats.dirs += 1
    identity = _identity(info)
    if trace and identity in seen:
        node.cycle = True
        return node

    expand = options.max_depth is None or depth < options.max_depth
    if expand:
        branch = seen | {identity} if trace else seen
        _fill(node, options, stats, branch, depth + 1)
    return node


def _keep(entry: "os.DirEntry[str]", relative: str, options: WalkOptions) -> bool:
    """Apply the dotfile, dirs-only and ignore rules to one entry.

    Ignore patterns are matched against the path relative to the scan root,
    which is why *relative* is threaded through from the caller.  A pattern
    that names a directory also hides everything below it, so directories are
    matched with ``is_dir=True`` and their parents have already been dropped.
    """
    if not options.show_hidden and entry.name.startswith("."):
        return False
    if options.dirs_only and not _is_dir(entry, options.follow_symlinks):
        return False
    if options.ignore is not None and options.ignore.matches(relative, _is_dir(entry, False)):
        return False
    return True


def _is_dir(entry: "os.DirEntry[str]", follow: bool) -> bool:
    try:
        return entry.is_dir(follow_symlinks=follow)
    except OSError:
        return False


def _sorted(
    entries: List["os.DirEntry[str]"],
    options: WalkOptions,
) -> List["os.DirEntry[str]"]:
    """Sort entries according to ``options.sort_key``."""
    if options.sort_key == "none":
        return list(entries)

    def key(entry: "os.DirEntry[str]") -> tuple:
        name = entry.name.lower()
        if options.sort_key == "name":
            return (name,)
        try:
            info = entry.stat(follow_symlinks=False)
            size, mtime = info.st_size, info.st_mtime
        except OSError:
            size, mtime = -1, 0.0
        if options.sort_key == "size":
            return (size, name)
        return (mtime, name)

    return sorted(entries, key=key, reverse=options.reverse)


def _identity(info: os.stat_result) -> _Identity:
    """The ``(device, inode)`` pair used to recognise a directory again."""
    return (info.st_dev, info.st_ino)


def _read_link(path: str) -> Optional[str]:
    try:
        return os.readlink(path)
    except OSError:
        return None


def _report(options: WalkOptions, path: str, error: OSError) -> None:
    if options.error_hook is not None:
        options.error_hook(path, error)
