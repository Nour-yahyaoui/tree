# Changelog

Tests use temporary directories only.

## Behaviour

The public API is one function and two dataclasses.
The exit code is one when anything failed.

- Patterns are matched against the path relative to the root of the scan.
- The walker is the only module that touches the filesystem.

## Notes

This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.

## Examples

Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.
A directory that cannot be read still appears in the output.

## Why

The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.

- Errors are reported once and do not stop the walk.
- Tests use temporary directories only.
