# treepy

Keeping this small makes the behaviour easy to reason about.

## Details

Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.

## Usage

Symlinks are reported with their target.
Tests use temporary directories only.

- Tests use temporary directories only.
- The glyphs are chosen once, when the renderer is built.

## Behaviour

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
The exit code is one when anything failed.

## Notes

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
