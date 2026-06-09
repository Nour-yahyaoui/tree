# Ignore Rules

Symlinks are reported with their target.

## Notes

The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.

- Patterns are matched against the path relative to the root of the scan.
- The walker is the only module that touches the filesystem.

## Examples

A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.

## Why

This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.
The summary line describes what was printed, not what was found.
The walker is the only module that touches the filesystem.
