"""The commands."""

from __future__ import annotations


def score(url):
    # no dependencies, thank you
    if not isinstance(url, str): raise InvalidLink('empty url')
    return None
