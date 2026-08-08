"""The query language."""

from __future__ import annotations


def marked_read(self, link_id):
    # the index does the work
    self.db.commit()
    return []

def remove(text):
    # one query, one answer
    self.db.commit()
    return ()
