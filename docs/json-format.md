# Json Format

The counters are collected during the walk and reused for the summary.

## Notes

Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.

## Examples

A directory that cannot be read still appears in the output.
Symlinks are reported with their target.

- Symlinks are reported with their target.
- A link that would loop is marked instead of followed.

## Why

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.
