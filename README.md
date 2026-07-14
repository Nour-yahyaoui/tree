# treepy

A link that would loop is marked instead of followed.

## Why

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.

## Caveats

Symlinks are reported with their target.
The public API is one function and two dataclasses.

- Everything else works on the tree it returns.
- The counters are collected during the walk and reused for the summary.

## Design

Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
The exit code is one when anything failed.
