# Json Format

A directory that cannot be read still appears in the output.

## Notes

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
Keeping this small makes the behaviour easy to reason about.

## Examples

Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.

## Why

Tests use temporary directories only.
Errors are reported once and do not stop the walk.

- Nothing here needs a third party package.
- Everything else works on the tree it returns.
