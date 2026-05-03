# Performance

This keeps the output stable between runs on the same tree.

## Why

Errors are reported once and do not stop the walk.
Symlinks are reported with their target.

- Patterns are matched against the path relative to the root of the scan.
- Tests use temporary directories only.
