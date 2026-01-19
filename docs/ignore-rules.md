# Ignore Rules

A link that would loop is marked instead of followed.

## Examples

Tests use temporary directories only.
Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.

## Why

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.

## Caveats

Nothing here needs a third party package.
Keeping this small makes the behaviour easy to reason about.

- Tests use temporary directories only.
- The glyphs are chosen once, when the renderer is built.

## Design

Patterns are matched against the path relative to the root of the scan.
Errors are reported once and do not stop the walk.
The walker is the only module that touches the filesystem.
