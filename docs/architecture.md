# Architecture

treepy is small enough to read in one sitting. The point of splitting it
into six modules is that each one can be replaced on its own: the text
renderer knows nothing about the filesystem, the walker knows nothing about
formatting, and the pattern matcher knows nothing about either.

## The pieces

```
cli.py ──▶ walker.py ──▶ node.py
  │            │
  │            └──▶ ignore.py
  └──▶ render.py ──▶ style.py
```

The arrows are imports. There are no cycles and no callbacks that travel
back up the stack, with one deliberate exception: the walker accepts an
`error_hook` so the CLI can decide how to report unreadable entries without
the walker importing `sys`.

## node.py

Two dataclasses and no logic worth mentioning. `Node` carries the fields the
renderers need (`name`, `size`, `mtime`, `symlink`, `link_target`, `cycle`,
`error`) plus `relative`, the path used by the ignore matcher. `Stats`
carries the counters for the summary line.

Keeping `Node` dumb means the renderers never touch the disk. That is why
`render_text` can be tested with hand-built trees, and why the JSON output
can be produced for a subtree that was filtered after the walk.

## walker.py

The only module that calls `os`. Most of the code exists to avoid getting
stuck or crashing:

- `walk()` handles the root, which may be a file, a symlink or missing.
- `_fill()` reads one directory, applies `_keep()` and attaches survivors.
- `_visit()` turns a single `DirEntry` into a `Node`.
- `_sorted()` applies the sort key, tolerating entries that cannot be
  stat'ed by falling back to a size of `-1` and a timestamp of `0`.

Symlink cycles are tracked with the `(st_dev, st_ino)` pair of every
directory on the current path, not of every directory ever seen. That
distinction matters: two sibling links to the same directory are fine, a
link that points at its own ancestor is not.

`WalkOptions` validates its own arguments in `__post_init__`, so a bad sort
key fails at construction time with a clear message instead of returning a
strange tree later.

## ignore.py

`Pattern.parse()` compiles one line of a `.gitignore` file into a regular
expression, remembering three things: whether the pattern was negated,
whether it only applies to directories, and whether it was anchored (which
git decides by the presence of a slash anywhere in the pattern).

`IgnoreSet` keeps the patterns in order because the last matching pattern
wins. `filter_tree()` and `prune_tree()` are the two post-walk filters; the
first one subtracts the entries it drops from the `Stats` it is given, so
the summary line keeps matching the printed tree.

## render.py

`render_text()` walks the tree once and appends one line per node,
accumulating the connector prefix as it descends. `render_json()` reuses
`node_to_dict()` so both renderers agree on what a node looks like.

`human_size()` is deliberately written to match the output of the C `tree`
utility (`1.0K`, `1.5M`) rather than decimal SI units, because that is what
people compare against.

## style.py

Whether colour is available is decided once, in `build_style()`, from the
`--color` flag, `isatty()`, `NO_COLOR` and `TERM`. Everything downstream
receives a `Style` object, which makes coloured output testable: build
`Style(enabled=True)` and assert on the escape sequences, or use
`plain_style()` and assert on plain strings.

## cli.py

`build_parser()` returns the parser and `main()` does the work, in this
order: build the ignore matcher, walk every requested path into the same
`Stats`, apply the post-walk filters, build `RenderOptions`, render, write.

The exit code is `1` when any entry failed to stat or read, and `0`
otherwise. Arguing with a tree printer about errors is not useful; the
stderr line and the `errors` counter are enough.
