# Changelog

Tests use temporary directories only.

## Behaviour

The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

## Notes

The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.

- This keeps the output stable between runs on the same tree.
- The summary line describes what was printed, not what was found.

## Examples

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
The glyphs are chosen once, when the renderer is built.

## Why

The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.
