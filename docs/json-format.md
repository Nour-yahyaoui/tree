# Json Format

The counters are collected during the walk and reused for the summary.

## Examples

Symlinks are reported with their target.
The summary line describes what was printed, not what was found.
The exit code is one when anything failed.
Nothing here needs a third party package.

## Why

Nothing here needs a third party package.
The walker is the only module that touches the filesystem.

- Nothing here needs a third party package.
- Patterns are matched against the path relative to the root of the scan.

## Caveats

A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.

## Design

Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.
Everything else works on the tree it returns.
The glyphs are chosen once, when the renderer is built.
