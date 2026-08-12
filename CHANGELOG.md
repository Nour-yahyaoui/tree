# Changelog

Nothing here needs a third party package.

## Examples

The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.

- Nothing here needs a third party package.
- Errors are reported once and do not stop the walk.

## Why

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.

## Caveats

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.

## Design

The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.

- Everything else works on the tree it returns.
- The counters are collected during the walk and reused for the summary.
