"""The small data structures shared by the walker and the renderers.

The tree treepy builds is intentionally boring: one :class:`Node` per
filesystem entry plus a :class:`Stats` counter for the summary line.  Keeping
these two objects dumb means the renderers never need to touch the disk and
the walker never needs to know how to format anything.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, List, Optional

__all__ = ["Node", "Stats"]


@dataclass
class Node:
    """A single filesystem entry, plus its children when it is a directory.

    ``relative`` is the path relative to the root of the scan (``""`` for the
    root itself).  The ignore matcher works on relative paths, which is why
    the walker keeps them around instead of recomputing them later.
    """

    name: str
    path: str
    is_dir: bool
    size: int = 0
    mtime: float = 0.0
    relative: str = ""
    symlink: bool = False
    link_target: Optional[str] = None
    cycle: bool = False
    error: Optional[str] = None
    children: List["Node"] = field(default_factory=list)

    def add(self, child: "Node") -> "Node":
        """Append *child* and return it, so recursive calls stay short."""
        self.children.append(child)
        return child

    def walk(self) -> Iterator["Node"]:
        """Yield this node, then every descendant, depth first."""
        yield self
        for child in self.children:
            yield from child.walk()

    def total_size(self) -> int:
        """Sum of the sizes of this node and all of its descendants."""
        if not self.is_dir:
            return self.size
        return sum(child.total_size() for child in self.children)

    def find(self, relative: str) -> Optional["Node"]:
        """Return the descendant whose relative path is *relative*, if any."""
        for node in self.walk():
            if node.relative == relative:
                return node
        return None


@dataclass
class Stats:
    """Counters collected while walking, used for the summary line."""

    dirs: int = 0
    files: int = 0
    symlinks: int = 0
    errors: int = 0
    total_bytes: int = 0

    def as_dict(self) -> dict:
        return {
            "directories": self.dirs,
            "files": self.files,
            "symlinks": self.symlinks,
            "errors": self.errors,
            "bytes": self.total_bytes,
        }

    def summary(self) -> str:
        """A human readable one-liner, e.g. ``3 directories, 12 files``."""
        dirs = "directory" if self.dirs == 1 else "directories"
        files = "file" if self.files == 1 else "files"
        parts = [f"{self.dirs} {dirs}", f"{self.files} {files}"]
        if self.symlinks:
            parts.append(f"{self.symlinks} symlinks")
        if self.errors:
            parts.append(f"{self.errors} errors")
        return ", ".join(parts)
