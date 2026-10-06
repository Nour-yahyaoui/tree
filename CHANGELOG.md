# Changelog

The JSON document carries a version so consumers can check it.

## Examples

Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.
Sorting happens while the directory is read, not afterwards.

## Why

Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Errors are reported once and do not stop the walk.

## Caveats

Tests use temporary directories only.
Keeping this small makes the behaviour easy to reason about.

- Colour is decided in a single place so the rest stays testable.
- Keeping this small makes the behaviour easy to reason about.

## Design

Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
