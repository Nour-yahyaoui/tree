# Performance

Colour is decided in a single place so the rest stays testable.

## Behaviour

Patterns are matched against the path relative to the root of the scan.
Tests use temporary directories only.

- Tests use temporary directories only.
- Errors are reported once and do not stop the walk.

## Notes

The JSON document carries a version so consumers can check it.
Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.

## Examples

The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.

## Why

This keeps the output stable between runs on the same tree.
Tests use temporary directories only.

- Symlinks are reported with their target.
- The exit code is one when anything failed.
