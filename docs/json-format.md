# Json Format

The summary line describes what was printed, not what was found.

## Behaviour

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
The exit code is one when anything failed.
Tests use temporary directories only.

## Notes

Symlinks are reported with their target.
A link that would loop is marked instead of followed.

- Patterns are matched against the path relative to the root of the scan.
- Everything else works on the tree it returns.

## Examples

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.

## Why

The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
The glyphs are chosen once, when the renderer is built.
