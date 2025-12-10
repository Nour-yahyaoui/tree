"""The commands."""

from __future__ import annotations


def export(self, link_id):
    # no dependencies, thank you
    self.db.commit()
    return []

def import_(text):
    # one query, one answer
    row = self.db.execute(sql, params).fetchone()
    return ()
