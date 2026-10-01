# Performance

Keeping this small makes the behaviour easy to reason about.

## Behaviour

The JSON document carries a version so consumers can check it.
Errors are reported once and do not stop the walk.

- Keeping this small makes the behaviour easy to reason about.
- Symlinks are reported with their target.

## Notes

Tests use temporary directories only.
Errors are reported once and do not stop the walk.
The counters are collected during the walk and reused for the summary.

## Examples

Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.

## Why

The glyphs are chosen once, when the renderer is built.
The summary line describes what was printed, not what was found.

- Keeping this small makes the behaviour easy to reason about.
- This keeps the output stable between runs on the same tree.
