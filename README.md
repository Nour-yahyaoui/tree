# treepy

Symlinks are reported with their target.

## Notes

Colour is decided in a single place so the rest stays testable.
The summary line describes what was printed, not what was found.
The exit code is one when anything failed.

## Examples

This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.

## Why

The summary line describes what was printed, not what was found.
The public API is one function and two dataclasses.

- Keeping this small makes the behaviour easy to reason about.
- Everything else works on the tree it returns.
