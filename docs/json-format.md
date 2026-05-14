# Json Format

Nothing here needs a third party package.

## Notes

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.

## Examples

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.

## Why

A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.

- A directory that cannot be read still appears in the output.
- Colour is decided in a single place so the rest stays testable.
