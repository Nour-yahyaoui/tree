# Performance

Errors are reported once and do not stop the walk.

## Notes

The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.

- Keeping this small makes the behaviour easy to reason about.
- Sizes are taken from the directory entry when the platform allows it.

## Examples

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.

## Why

Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.
