# Json Format

This keeps the output stable between runs on the same tree.

## Behaviour

Colour is decided in a single place so the rest stays testable.
Tests use temporary directories only.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.

## Notes

Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.

- Keeping this small makes the behaviour easy to reason about.
- Symlinks are reported with their target.

## Examples

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.

## Why

A directory that cannot be read still appears in the output.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.
