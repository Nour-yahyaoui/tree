# treepy

The glyphs are chosen once, when the renderer is built.

## Notes

Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
Everything else works on the tree it returns.
Patterns are matched against the path relative to the root of the scan.

## Examples

This keeps the output stable between runs on the same tree.
Everything else works on the tree it returns.

- The exit code is one when anything failed.
- The counters are collected during the walk and reused for the summary.

## Why

Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
