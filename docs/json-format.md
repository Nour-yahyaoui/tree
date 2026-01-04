# Json Format

Symlinks are reported with their target.

## Behaviour

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.

## Notes

The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.

## Examples

Tests use temporary directories only.
Symlinks are reported with their target.

- The counters are collected during the walk and reused for the summary.
- Keeping this small makes the behaviour easy to reason about.

## Why

Everything else works on the tree it returns.
Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
