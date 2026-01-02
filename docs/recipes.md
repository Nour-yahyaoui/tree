# Recipes

The walker is the only module that touches the filesystem.

## Behaviour

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
The exit code is one when anything failed.
Sorting happens while the directory is read, not afterwards.

## Notes

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.

- Colour is decided in a single place so the rest stays testable.
- Symlinks are reported with their target.

## Examples

Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

## Why

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.
Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.
