"""ANSI colour helpers.

The decision of whether colour is available is made exactly once, in
:func:`build_style`, and the renderer only ever sees a :class:`Style` object.
That keeps the renderer free of ``isatty`` checks and makes coloured output
easy to assert on in tests.
"""

from __future__ import annotations

import os
import sys
from dataclasses import dataclass, field
from typing import Mapping, Optional

__all__ = ["Style", "plain_style", "build_style", "EXTENSION_COLOURS"]

RESET = "\033[0m"

#: Colours used for common file extensions, as 256 colour palette indexes.
EXTENSION_COLOURS: Mapping[str, int] = {
    ".py": 33,
    ".pyi": 33,
    ".md": 245,
    ".rst": 245,
    ".txt": 250,
    ".json": 178,
    ".toml": 178,
    ".yaml": 178,
    ".yml": 178,
    ".ini": 178,
    ".cfg": 178,
    ".sh": 114,
    ".bash": 114,
    ".html": 208,
    ".css": 105,
    ".js": 220,
    ".ts": 39,
    ".rs": 209,
    ".c": 68,
    ".h": 68,
    ".go": 45,
    ".sql": 141,
    ".png": 170,
    ".jpg": 170,
    ".jpeg": 170,
    ".gif": 170,
    ".svg": 170,
    ".pdf": 124,
    ".zip": 137,
    ".tar": 137,
    ".gz": 137,
}


@dataclass
class Style:
    """A tiny wrapper that paints strings, or leaves them alone."""

    enabled: bool = True
    directory_colour: int = 34
    symlink_colour: int = 37
    error_colour: int = 31
    executable_colour: int = 118
    extension_colours: Mapping[str, int] = field(
        default_factory=lambda: dict(EXTENSION_COLOURS)
    )

    def paint(self, text: str, colour: Optional[int]) -> str:
        if not self.enabled or colour is None:
            return text
        return f"\033[38;5;{colour}m{text}{RESET}"

    def directory(self, text: str) -> str:
        return self.paint(text, self.directory_colour)

    def symlink(self, text: str) -> str:
        return self.paint(text, self.symlink_colour)

    def error(self, text: str) -> str:
        return self.paint(text, self.error_colour)

    def file(self, name: str, executable: bool = False) -> str:
        if executable:
            return self.paint(name, self.executable_colour)
        _, extension = os.path.splitext(name)
        return self.paint(name, self.extension_colours.get(extension.lower()))

    def colour_for(self, name: str) -> Optional[int]:
        """The palette index a name would be painted with, if any."""
        if "." not in name:
            return None
        _, extension = os.path.splitext(name)
        return self.extension_colours.get(extension.lower())


def plain_style() -> Style:
    """A style that never emits escape sequences."""
    return Style(enabled=False)


def build_style(mode: str = "auto", stream=None) -> Style:
    """Build a style from ``--color`` mode: auto, always or never."""
    if mode not in ("auto", "always", "never"):
        raise ValueError(f"unknown colour mode {mode!r}")
    if mode == "always":
        return Style(enabled=True)
    if mode == "never":
        return plain_style()
    stream = stream if stream is not None else sys.stdout
    interactive = bool(getattr(stream, "isatty", lambda: False)())
    if not interactive:
        return plain_style()
    if os.environ.get("NO_COLOR"):
        return plain_style()
    if os.environ.get("TERM", "") in ("", "dumb"):
        return plain_style()
    return Style(enabled=True)
