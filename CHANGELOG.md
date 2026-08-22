# Changelog

Everything else works on the tree it returns.

## Examples

A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.

## Why

The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
