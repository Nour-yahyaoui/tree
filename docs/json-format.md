# Json Format

The walker is the only module that touches the filesystem.

## Notes

Errors are reported once and do not stop the walk.
Tests use temporary directories only.

- Symlinks are reported with their target.
- Patterns are matched against the path relative to the root of the scan.

## Examples

The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.

## Why

Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
A directory that cannot be read still appears in the output.
