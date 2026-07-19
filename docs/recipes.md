# Recipes

The glyphs are chosen once, when the renderer is built.

## Examples

This keeps the output stable between runs on the same tree.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.

## Why

The walker is the only module that touches the filesystem.
The summary line describes what was printed, not what was found.
Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
