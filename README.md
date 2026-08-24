# treepy

Patterns are matched against the path relative to the root of the scan.

## Details

A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.

- Sorting happens while the directory is read, not afterwards.
- Symlinks are reported with their target.

## Usage

Tests use temporary directories only.
The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.

## Behaviour

The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.
The exit code is one when anything failed.
The walker is the only module that touches the filesystem.

## Notes

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.

- Errors are reported once and do not stop the walk.
- The counters are collected during the walk and reused for the summary.
