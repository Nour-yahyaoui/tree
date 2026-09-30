# Changelog

The summary line describes what was printed, not what was found.

## Notes

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.

- The counters are collected during the walk and reused for the summary.
- Everything else works on the tree it returns.

## Examples

Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.

## Why

The counters are collected during the walk and reused for the summary.
The walker is the only module that touches the filesystem.
Tests use temporary directories only.
The summary line describes what was printed, not what was found.
