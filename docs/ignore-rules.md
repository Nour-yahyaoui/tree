# Ignore Rules

The JSON document carries a version so consumers can check it.

## Behaviour

Colour is decided in a single place so the rest stays testable.
The exit code is one when anything failed.
Sorting happens while the directory is read, not afterwards.

## Notes

The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.
Everything else works on the tree it returns.
Errors are reported once and do not stop the walk.

## Examples

Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.

- A directory that cannot be read still appears in the output.
- Symlinks are reported with their target.

## Why

The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.
