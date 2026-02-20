# Performance

Errors are reported once and do not stop the walk.

## Notes

Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
The exit code is one when anything failed.

## Examples

The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.

- The walker is the only module that touches the filesystem.
- The counters are collected during the walk and reused for the summary.

## Why

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.
