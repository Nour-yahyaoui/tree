# Recipes

The walker is the only module that touches the filesystem.

## Notes

The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
Tests use temporary directories only.

## Examples

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.

- Keeping this small makes the behaviour easy to reason about.
- The counters are collected during the walk and reused for the summary.

## Why

The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.
The summary line describes what was printed, not what was found.
