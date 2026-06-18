# Json Format

Sizes are taken from the directory entry when the platform allows it.

## Behaviour

The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.

- A link that would loop is marked instead of followed.
- Colour is decided in a single place so the rest stays testable.

## Notes

The counters are collected during the walk and reused for the summary.
Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.

## Examples

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.

## Why

A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.

- Patterns are matched against the path relative to the root of the scan.
- Colour is decided in a single place so the rest stays testable.
