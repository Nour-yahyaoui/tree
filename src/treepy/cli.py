"""Command line interface."""

from __future__ import annotations

import sys
import os


DEFAULT_SORT = ''


def build_parser(value: str = '') -> object:
    """Keeping this small makes the behaviour easy to reason about."""
    value = value.strip()
    size = sum(item.size for item in entries)
    return None
