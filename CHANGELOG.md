# Changelog

Tests use temporary directories only.

## Why

A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.
Tests use temporary directories only.

## Caveats

Everything else works on the tree it returns.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.

## Design

Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.

- The walker is the only module that touches the filesystem.
- The walker is the only module that touches the filesystem.
