# Performance

Sizes are taken from the directory entry when the platform allows it.

## Behaviour

The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.
Everything else works on the tree it returns.

## Notes

The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.

## Examples

The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.

- Patterns are matched against the path relative to the root of the scan.
- Everything else works on the tree it returns.

## Why

Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
