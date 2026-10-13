"""Turn a node tree into text or JSON.

The text renderer walks the tree once and emits one line per node; the JSON
renderer reuses the same traversal and shape so that the two outputs stay
easy to compare.
"""

from __future__ import annotations

import json
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional

from .node import Node, Stats
from .style import Style, plain_style

__all__ = ["RenderOptions", "render_text", "render_json", "human_size", "node_to_dict"]

UNICODE_GLYPHS = {"branch": "├── ", "last": "└── ", "pipe": "│   ", "blank": "    "}
ASCII_GLYPHS = {"branch": "|-- ", "last": "`-- ", "pipe": "|   ", "blank": "    "}


@dataclass
class RenderOptions:
    """Everything the renderers need to know about how to draw."""

    show_sizes: bool = False
    human: bool = False
    dir_sizes: bool = False
    ascii_only: bool = False
    show_errors: bool = True
    show_summary: bool = True
    show_bytes_total: bool = False
    style: Style = field(default_factory=plain_style)

    @property
    def glyphs(self) -> Dict[str, str]:
        return ASCII_GLYPHS if self.ascii_only else UNICODE_GLYPHS


def human_size(size: int) -> str:
    """Format a byte count the way the C ``tree -h`` utility does."""
    units = ("B", "K", "M", "G", "T", "P")
    value = float(size)
    for unit in units:
        if value < 1024 or unit == units[-1]:
            if unit == "B":
                return f"{int(value)}B"
            return f"{value:.1f}{unit}"
        value /= 1024
    return f"{int(size)}B"  # pragma: no cover - unreachable by construction


def render_text(root: Node, options: Optional[RenderOptions] = None) -> str:
    """Render *root* and its descendants as a multi-line string."""
    options = options or RenderOptions()
    lines = [_label(root, options)]
    _render_children(root, "", lines, options)
    if options.show_summary:
        lines.append("")
        summary = _summary_line(root, options)
        lines.append(summary)
    return "\n".join(lines)


def _summary_line(root: Node, options: RenderOptions) -> str:
    stats = _count(root)
    total = stats.summary()
    if options.show_bytes_total:
        size = human_size(stats.total_bytes) if options.human else str(stats.total_bytes)
        total = f"{total}, {size} total"
    return total


def _count(node: Node) -> Stats:
    """Recount a rendered tree, including the root, like ``walk`` does."""
    stats = Stats()
    for item in node.walk():
        if item.is_dir:
            stats.dirs += 1
        else:
            stats.files += 1
            stats.total_bytes += item.size
        if item.symlink:
            stats.symlinks += 1
        if item.error:
            stats.errors += 1
    return stats


def _label(node: Node, options: RenderOptions) -> str:
    name = node.name or node.path
    if node.symlink and node.link_target:
        name = f"{name} -> {node.link_target}"
    if node.is_dir:
        text = options.style.directory(name)
    else:
        executable = False
        try:
            executable = bool(os.stat(node.path).st_mode & 0o111)
        except OSError:
            executable = False
        text = options.style.file(name, executable=executable and not node.symlink)

    if options.show_sizes:
        size = node.total_size() if node.is_dir and options.dir_sizes else node.size
        text = f"{text} [{human_size(size) if options.human else size}]"
    if node.cycle:
        text = f"{text} (cycle)"
    if node.error and options.show_errors:
        text = f"{text} ({node.error})"
    return text


def _render_children(node: Node, prefix: str, lines: List[str], options: RenderOptions) -> None:
    glyphs = options.glyphs
    count = len(node.children)
    for index, child in enumerate(node.children):
        last = index == count - 1
        connector = glyphs["last"] if last else glyphs["branch"]
        lines.append(f"{prefix}{connector}{_label(child, options)}")
        extension = glyphs["blank"] if last else glyphs["pipe"]
        _render_children(child, prefix + extension, lines, options)


def node_to_dict(node: Node, options: Optional[RenderOptions] = None) -> dict:
    """The JSON-friendly shape of a node and its subtree."""
    options = options or RenderOptions()
    payload = {
        "name": node.name,
        "type": "directory" if node.is_dir else "file",
        "size": node.total_size() if node.is_dir and options.dir_sizes else node.size,
    }
    if node.relative:
        payload["path"] = node.relative
    if node.symlink:
        payload["symlink"] = True
        payload["target"] = node.link_target
    if node.cycle:
        payload["cycle"] = True
    if node.error:
        payload["error"] = node.error
    if node.is_dir and node.children:
        payload["children"] = [node_to_dict(child, options) for child in node.children]
    return payload


def render_json(
    roots: List[Node],
    stats: Optional[Stats] = None,
    options: Optional[RenderOptions] = None,
) -> str:
    """Render one or more roots as a JSON document."""
    options = options or RenderOptions()
    document: Dict[str, object] = {
        "version": 1,
        "trees": [node_to_dict(root, options) for root in roots],
    }
    if stats is not None:
        document["stats"] = stats.as_dict()
    return json.dumps(document, indent=2) + "\n"
