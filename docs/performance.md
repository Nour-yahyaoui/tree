# Performance

treepy is a single pass over the filesystem with no caches and no threads.
The numbers below were measured on a cold page cache over an SSD with
Python 3.11, and they are the reason a few of the decisions in the walker
look the way they do.

## The short version

| Tree | Entries | `treepy` | `tree(1)` |
| --- | --- | --- | --- |
| treepy itself | ~60 | 0.03 s | 0.01 s |
| a CPython checkout | ~35 k | 0.9 s | 0.2 s |
| a large `node_modules` | ~180 k | 6.4 s | 1.4 s |

Most of the gap against the C utility is interpreter start-up plus one
`stat` per entry; the walk itself is not doing anything clever, and it is
not trying to.

## What costs time

- **`scandir` beats `listdir`.** `os.scandir` reuses the directory entry
  information from `readdir`, so `is_dir()` does not need a `stat` on most
  filesystems. Everything else is a `stat` per entry, unavoidable to get
  sizes and timestamps.
- **Sorting by size or mtime forces a `stat` on every entry** of every
  directory, even the ones the sort would drop. Sorting by name costs
  nothing: the name is already in hand.
- **`--du` adds a second pass** over the in-memory tree to sum sizes. It is
  cheap compared to the walk, but it does mean the numbers in the summary
  and the numbers on the nodes are computed at different times.
- **`--follow-links` makes cycles possible,** so every directory on the
  current path is remembered and compared. The set stays small — it is the
  depth, not the width, of the tree.

## What was deliberately left out

- **No threading.** On a warm cache the walk is CPU-bound in the
  interpreter, and on a cold cache it is bound by the disk. Threads help
  with neither, and they would make the deterministic ordering of the
  output much harder to guarantee.
- **No caching of `stat` results.** A tree printer that reports stale
  sizes is worse than one that is 20% slower.
- **No early exit on the first error.** A tree with one unreadable
  directory is still a useful tree; the error is reported and the count is
  incremented.

## Measuring

```sh
python3 -m timeit -n 5 -s 'from treepy import walk' 'walk("src", None)'
```

For a profile of a real tree, `cProfile` is enough:

```sh
python3 -m cProfile -s cumtime -m treepy -L 6 /usr/lib/python3.11 > /dev/null
```

The profile is dominated by `os.scandir`, `os.stat` and `posix.readdir`, in
that order, which is what you would expect from a program whose whole job is
to look at every entry exactly once.
