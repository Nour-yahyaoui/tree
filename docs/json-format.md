# Json Format

The public API is one function and two dataclasses.

## Examples

Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.

- Everything else works on the tree it returns.
- The glyphs are chosen once, when the renderer is built.

## Why

Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.

## Caveats

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.

## Design

The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

- The glyphs are chosen once, when the renderer is built.
- The exit code is one when anything failed.
