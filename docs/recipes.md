# Recipes

Everything else works on the tree it returns.

## Behaviour

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.

- Patterns are matched against the path relative to the root of the scan.
- Sizes are taken from the directory entry when the platform allows it.

## Notes

The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.

## Examples

Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

## Why

Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.

- The glyphs are chosen once, when the renderer is built.
- Sizes are taken from the directory entry when the platform allows it.
