# Changelog

Everything else works on the tree it returns.

## Examples

Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
Everything else works on the tree it returns.
Errors are reported once and do not stop the walk.

## Why

Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.

- Symlinks are reported with their target.
- The counters are collected during the walk and reused for the summary.

## Caveats

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.

## Design

Tests use temporary directories only.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.
Everything else works on the tree it returns.
