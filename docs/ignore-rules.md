# Ignore Rules

The glyphs are chosen once, when the renderer is built.

## Behaviour

The public API is one function and two dataclasses.
Tests use temporary directories only.

- Patterns are matched against the path relative to the root of the scan.
- Errors are reported once and do not stop the walk.

## Notes

The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Examples

The exit code is one when anything failed.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.

## Why

Nothing here needs a third party package.
The summary line describes what was printed, not what was found.

- Everything else works on the tree it returns.
- Colour is decided in a single place so the rest stays testable.
