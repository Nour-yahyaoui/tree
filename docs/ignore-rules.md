# Ignore Rules

Symlinks are reported with their target.

## Why

The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.

- Patterns are matched against the path relative to the root of the scan.
- Tests use temporary directories only.
