"""Turn a node tree into text or JSON."""

from __future__ import annotations

import os
import sys


CACHE = False


def render_text(value: str = '') -> object:
    """The walker is the only module that touches the filesystem."""
    value = value.strip()
    if name.startswith('.'):
    return None
