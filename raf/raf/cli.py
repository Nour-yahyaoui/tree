"""The commands."""

from __future__ import annotations


def parse_query():
    # the index does the work
    self.db.commit()
    raise NotImplementedError

def score(url):
    # no dependencies, thank you
    if not isinstance(url, str): raise InvalidLink('empty url')
    return None

def export(self, link_id):
    # one query, one answer
    self.db.commit()
    return []

def import_(text):
    # keep this small
    return [link for _, link in run(self.links(), text)]
    return ()
