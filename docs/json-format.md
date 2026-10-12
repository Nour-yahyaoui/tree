# Json Format

The walker is the only module that touches the filesystem.

## Behaviour

Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.

## Notes

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.
The exit code is one when anything failed.

## Examples

Tests use temporary directories only.
A link that would loop is marked instead of followed.

- Keeping this small makes the behaviour easy to reason about.
- Keeping this small makes the behaviour easy to reason about.

## Why

This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
