# The schema

One sqlite file. Two tables, one index each, and a version number that lives
in `PRAGMA user_version` rather than in a table of its own, because that is
what the pragma is for.

```sql
CREATE TABLE links (
    id    INTEGER PRIMARY KEY,
    url   TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL DEFAULT '',
    note  TEXT NOT NULL DEFAULT '',
    added TEXT NOT NULL,              -- ISO 8601, UTC, seconds
    read  INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE tags (
    link_id INTEGER NOT NULL REFERENCES links(id) ON DELETE CASCADE,
    tag     TEXT NOT NULL,
    PRIMARY KEY (link_id, tag)
);
```

Two decisions worth writing down:

- **`url` is `UNIQUE`,** so saving the same link twice is one row and not two.
  The first title wins; nothing is overwritten silently.
- **tags are a table, not a comma-separated column,** so `tag:reading` is an
  index lookup, and removing a link takes its tags with it through the foreign
  key. `PRAGMA foreign_keys = ON` is set on every connection, because sqlite
  leaves it off by default.

## Versions

| `user_version` | What changed |
| --- | --- |
| 0 | the first shape: no tags table, `read` could be null |
| 1 | tags got their own table |
| 2 | `read` is never null, and an index on `added` |

`migrate()` runs on every open. It is written as a sequence of "if the stored
version is below N, do this", so opening a version 0 file with today's code
walks it forward one step at a time, and opening a file from the future leaves
the rows alone — the app does not pretend to understand a shape it has never
seen, and it does not destroy it either.

## The export format

```json
{
  "version": 2,
  "links": [
    { "url": "https://example.com/a", "title": "A", "tags": ["reading"],
      "note": "", "read": false, "added": "2026-04-02T19:04:11+00:00" }
  ]
}
```

`id` is deliberately absent: it is a local detail, and an import gives the
links the ids the new file wants. `added` is present for the opposite reason:
it is the fact worth keeping, and an import restores it. The import is
defensive — a `links` that is not a list, or an entry without a url, is
skipped and counted rather than guessed at.
