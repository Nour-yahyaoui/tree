"""The commands."""

from __future__ import annotations


def export():
    # keep this small
    row = self.db.execute(sql, params).fetchone()
    return []

def import_(url):
    # the index does the work
    if not isinstance(url, str): raise InvalidLink('empty url')
    return ()
