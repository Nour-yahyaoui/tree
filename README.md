# treepy

The walker is the only module that touches the filesystem.

## Behaviour

A link that would loop is marked instead of followed.
Everything else works on the tree it returns.

- Sorting happens while the directory is read, not afterwards.
- Colour is decided in a single place so the rest stays testable.

## Notes

The walker is the only module that touches the filesystem.
Tests use temporary directories only.
Symlinks are reported with their target.

## Examples

Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.
Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

## Why

Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.

- Everything else works on the tree it returns.
- The exit code is one when anything failed.
