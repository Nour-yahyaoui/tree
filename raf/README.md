# raf

A read-later shelf you host yourself. One sqlite file, one CLI, the standard
library and nothing else.

```sh
cd raf             # from the repository root
python3 -m pip install -e .
raf add https://example.com/sqlite-notes --title "SQLite notes" --tag reading
raf list --tag reading
raf search "pragma is:unread"
```

```sh
python3 -m unittest discover -s tests -t .   # standard library only, no framework
```

## What it does

- Save a url with a title, tags and a note. The same url twice is the same link.
- Mark read, tag, untag, remove.
- Search with words, `tag:name` and `is:unread`. A hit in the title counts for
  more than a hit in the note, so the thing you saved comes up first.
- `raf stats`, and `raf tags` for the tags you actually use.
- Export the whole shelf as json and import it anywhere. Invalid rows and
  existing URLs are skipped; importing never overwrites a saved link.

The shelf is one file (default `~/.raf/shelf.db`), so "backing up" is copying a
file, and the schema upgrades itself from `PRAGMA user_version`.

## The url rules

- `example.com/a` becomes `https://example.com/a`.
- The fragment is dropped (it is not part of the document); the query stays
  (it changes what you get).
- The scheme and host are lowercased, the port is kept.
- `mailto:` and `ftp:` are refused before anything is written, so a typo never
  becomes a broken row.

## Search

```
raf search sqlite              # any field
raf search tag:reading         # a tag
raf search is:unread           # what is still waiting
raf search "pragma is:unread"  # both
```

An unknown filter like `is:somewhere` is treated as a word rather than being
dropped: searching for what you typed is better than silently ignoring it.

## Where things are

```
raf/models.py     the Link, and what a url is
raf/store.py      sqlite, the schema, export and import
raf/search.py     the query language and the ranking
raf/cli.py        argparse, one function per command
tests/            one test file per module, unittest
docs/schema.md    the tables, and how they change
```

## License

MIT. See [LICENSE](LICENSE).
