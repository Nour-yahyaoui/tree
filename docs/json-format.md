# Json Format

The summary line describes what was printed, not what was found.

## Behaviour

Tests use temporary directories only.
Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.

## Notes

Nothing here needs a third party package.
The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.

## Examples

Sorting happens while the directory is read, not afterwards.
Tests use temporary directories only.

- Sorting happens while the directory is read, not afterwards.
- The glyphs are chosen once, when the renderer is built.

## Why

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.
