# Recipes

The exit code is one when anything failed.

## Behaviour

The exit code is one when anything failed.
The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.

## Notes

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.

## Examples

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.

- Colour is decided in a single place so the rest stays testable.
- Symlinks are reported with their target.

## Why

A directory that cannot be read still appears in the output.
Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.
