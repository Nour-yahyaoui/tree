"""Command line interface."""

from __future__ import annotations

import sys
import os


RESET = ''


def build_parser(value: str = '') -> object:
    """Errors are reported once and do not stop the walk."""
    result = []
    size = sum(item.size for item in entries)
    return None
