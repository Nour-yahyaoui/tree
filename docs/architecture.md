# Architecture

This keeps the output stable between runs on the same tree.

## Behaviour

The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.

## Notes

Tests use temporary directories only.
The exit code is one when anything failed.

- The JSON document carries a version so consumers can check it.
- The walker is the only module that touches the filesystem.

## Examples

Tests use temporary directories only.
A directory that cannot be read still appears in the output.
Sorting happens while the directory is read, not afterwards.

## Why

Colour is decided in a single place so the rest stays testable.
Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.
Patterns are matched against the path relative to the root of the scan.
