# Recipes

The JSON document carries a version so consumers can check it.

## Behaviour

The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.

- The glyphs are chosen once, when the renderer is built.
- This keeps the output stable between runs on the same tree.

## Notes

This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.

## Examples

Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.

## Why

Nothing here needs a third party package.
A directory that cannot be read still appears in the output.

- Keeping this small makes the behaviour easy to reason about.
- Keeping this small makes the behaviour easy to reason about.
