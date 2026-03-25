# Architecture

Keeping this small makes the behaviour easy to reason about.

## Why

Tests use temporary directories only.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.

## Caveats

The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.
Symlinks are reported with their target.
The public API is one function and two dataclasses.

## Design

Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.

- The walker is the only module that touches the filesystem.
- The glyphs are chosen once, when the renderer is built.
