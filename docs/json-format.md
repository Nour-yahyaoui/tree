# Json Format

The glyphs are chosen once, when the renderer is built.

## Behaviour

Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.

## Notes

The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
Tests use temporary directories only.

## Examples

This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.

- The glyphs are chosen once, when the renderer is built.
- The exit code is one when anything failed.

## Why

Nothing here needs a third party package.
Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
