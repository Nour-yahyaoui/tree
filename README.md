# treepy

A link that would loop is marked instead of followed.

## Examples

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.

- This keeps the output stable between runs on the same tree.
- Colour is decided in a single place so the rest stays testable.

## Why

Colour is decided in a single place so the rest stays testable.
Everything else works on the tree it returns.
Sizes are taken from the directory entry when the platform allows it.

## Caveats

Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.

## Design

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.

- The counters are collected during the walk and reused for the summary.
- Tests use temporary directories only.
