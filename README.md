# treepy

A tiny, dependency-free directory tree printer for humans and machines.

`treepy` walks a directory, prints it as a tree, and can hand the same
structure to another program as JSON. It is one file-per-concern, has no
runtime dependencies, and runs on any Python 3.9+.

```
$ treepy -L 2 --size -H src
src [0B]
└── treepy [12.9K]
    ├── __init__.py [862B]
    ├── __main__.py [159B]
    ├── cli.py [6.2K]
    ├── ignore.py [5.9K]
    ├── node.py [2.8K]
    ├── render.py [5.3K]
    ├── style.py [3.3K]
    └── walker.py [7.6K]

2 directories, 8 files, 32.1K total
```

## Install

```sh
git clone https://github.com/Nour-yahyaoui/tree
cd tree
python3 -m pip install -e .
treepy --version
```

Nothing is required at runtime beyond the standard library. To run the
tests without installing anything:

```sh
make test        # python3 -m unittest discover -s tests -t .
make coverage    # optional, needs coverage.py
```

## Usage

```
treepy [paths ...] [options]
```

With no path, the current directory is printed. Several paths may be given;
each one is printed as its own tree and the summary lines add up.

### What to show

| Flag | Meaning |
| --- | --- |
| `-L N`, `--depth N` | descend at most `N` levels (`-L 0` prints the root only) |
| `-a`, `--all` | include dotfiles |
| `-d`, `--dirs-only` | list directories only |
| `-l`, `--follow-links` | follow symlinks, with cycle detection |
| `-I PATTERN`, `--exclude` | skip entries matching `PATTERN` (repeatable) |
| `-P PATTERN`, `--include` | show only entries matching `PATTERN` |
| `--gitignore` | honour the `.gitignore` file of each root |
| `--prune` | hide directories that end up with no children |
| `--max-entries N` | keep at most `N` children per directory |

`--exclude` and `--include` use `.gitignore`-style patterns: `*` stops at a
slash, `**` crosses it, a trailing `/` matches directories only, and a
leading `!` negates. See [docs/ignore-rules.md](docs/ignore-rules.md).

### Ordering

`--sort name|size|mtime|none` picks the sort key (default `name`, compared
case-insensitively); `-r`, `--reverse` flips it.

### Output

| Flag | Meaning |
| --- | --- |
| `-s`, `--size` | show the size of every entry in bytes |
| `-H`, `--human-readable` | print sizes as `1.5K`, `2.0M`, ... |
| `--du` | show directory totals instead of per-entry sizes |
| `--json` | emit the whole structure as JSON |
| `--ascii` | use `|--` and `` `-- `` instead of box drawing characters |
| `--color auto\|always\|never` | force or suppress ANSI colour |
| `-q`, `--quiet` | hide the summary line |
| `-o FILE`, `--output FILE` | write to a file instead of stdout |

## JSON output

`--json` prints one document containing every requested tree plus the
totals, which makes `treepy` usable in pipelines:

```sh
treepy --json src | jq '.trees[0].children[].name'
treepy --json -P '*.py' src | jq '.stats'
```

```json
{
  "version": 1,
  "trees": [
    {
      "name": "src",
      "type": "directory",
      "size": 0,
      "children": [
        { "name": "treepy", "type": "directory", "size": 0, "path": "treepy" }
      ]
    }
  ],
  "stats": { "directories": 2, "files": 8, "symlinks": 0, "errors": 0, "bytes": 32855 }
}
```

The exact shape is documented in [docs/json-format.md](docs/json-format.md).

## Behaviour worth knowing about

- **Symlinks are not followed by default.** They are printed with their
  target (`alias.txt -> real.txt`) and counted as symlinks, not files. With
  `--follow-links` a directory link is descended into, and the walker keeps
  the `(device, inode)` pair of every directory on the current path so a link
  that points back up the tree is marked `(cycle)` instead of looping.
- **Unreadable entries do not abort the walk.** They are printed with the
  error message and counted; the exit code becomes `1` and the message goes
  to stderr, exactly once per entry.
- **`-d` still walks into directories.** Only files are hidden, so the
  summary stays honest about the directories below.
- **`--prune` and `-P` change the counters.** Entries removed after the walk
  are subtracted from the summary, so the totals always describe what you
  can actually see on screen.

## Project layout

```
src/treepy/node.py     the Node/Stats dataclasses
src/treepy/walker.py   filesystem traversal, the only disk-touching module
src/treepy/ignore.py   .gitignore style pattern matching
src/treepy/style.py    ANSI colour helpers
src/treepy/render.py   text and JSON renderers
src/treepy/cli.py      argument parsing and the main() entry point
tests/                 unittest suite, no external dependencies
docs/                  notes on the internals
examples/              sample outputs
```

The dependency direction is one-way: `cli` → `walker` → `node`, with
`render` and `ignore` sitting beside the walker and never calling back into
the CLI. [docs/architecture.md](docs/architecture.md) explains the reasons.

## Development

```sh
make test        # unit tests
make lint        # compile every module (catches syntax errors)
make demo        # print this repository with treepy itself
make clean       # drop caches and build output
```

CI runs the suite on Python 3.9, 3.11 and 3.12 and smoke tests the CLI.
Changes are welcome; keep the zero-dependency promise intact.

## License

MIT. See [LICENSE](LICENSE).
