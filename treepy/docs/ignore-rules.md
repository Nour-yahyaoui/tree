# Ignore rules

`--exclude`/`-I` and `--include`/`-P` take one pattern each and may be
repeated (`-I` only; `-P` keeps the last one). `--gitignore` reads the
`.gitignore` of each requested root and adds its lines after the command
line patterns, so a `--exclude` on the command line can be undone by a `!`
line in the file, exactly like git.

## The dialect

| Pattern | Matches |
| --- | --- |
| `build` | any entry named `build`, at any depth |
| `build/` | directories named `build` only |
| `src/generated` | `src/generated` at the root of the scan only |
| `*.log` | any entry ending in `.log`, at any depth |
| `logs/*.log` | `.log` files directly inside `logs` |
| `**/cache` | `cache` at any depth, spelled the long way |
| `v[0-9].py` | `v0.py` ... `v9.py` |
| `!keep.log` | undoes an earlier match |

Rules of thumb:

- A slash anywhere in the pattern anchors it to the root of the scan.
- `*` stops at a slash, `**` crosses slashes, `?` matches one non-slash
  character.
- The last matching pattern wins, so put negations after the patterns they
  undo.
- Comments start with `#`; a blank line is ignored. A pattern that is only
  `!` or `/` is ignored as well.

## Patterns are matched on relative paths

The walker threads the path relative to the requested root through the
recursion and matches that, never the absolute path. This means:

```sh
treepy -I '*.pyc' .          # works the same from any directory
treepy -I '*/generated' src  # anchored at src/, not at the repository root
```

An ignored directory is not descended into, so patterns that name a
directory also hide everything below it — there is no way to ignore a
directory and re-include a file inside it, which matches git's behaviour.

## Ignore files are read, not inherited

`--gitignore` looks for `.gitignore` next to each path you asked for. It
does not walk down looking for nested ignore files: a tree printer that
started merging ignore files per directory would have to explain which file
produced which decision, and the answer is rarely interesting. If you need
that, `git ls-files` plus `treepy --include` gets you there.

## Interaction with the summary

`filter_tree()` removes nodes after the walk and adjusts the `Stats` it was
handed, so `treepy -P '*.py' -s` reports the number of files it actually
printed, not the number it found. Directories that lose all of their
children are pruned as well, since an empty directory in the output would
only raise the question of why it is there.
