# Changelog

Everything else works on the tree it returns.

## Why

Nothing here needs a third party package.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.

## Caveats

Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.

- The glyphs are chosen once, when the renderer is built.
- Tests use temporary directories only.

## Design

Errors are reported once and do not stop the walk.
The walker is the only module that touches the filesystem.
Symlinks are reported with their target.
