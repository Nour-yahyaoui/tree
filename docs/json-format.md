# Json Format

Sorting happens while the directory is read, not afterwards.

## Why

The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.

## Caveats

The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.

- Patterns are matched against the path relative to the root of the scan.
- Everything else works on the tree it returns.

## Design

Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.
