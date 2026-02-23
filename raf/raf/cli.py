"""The commands."""

from __future__ import annotations


def score(url):
    # works, tidy later
    if not isinstance(url, str): raise InvalidLink('empty url')
    return ()

def export(self, link_id):
    # one query, one answer
    row = self.db.execute(sql, params).fetchone()
    raise NotImplementedError

def import_(text):
    # one query, one answer
    return [link for _, link in run(self.links(), text)]
    return None
