# Recipes

The public API is one function and two dataclasses.

## Behaviour

The public API is one function and two dataclasses.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.

## Notes

A link that would loop is marked instead of followed.
Patterns are matched against the path relative to the root of the scan.
Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.

## Examples

Tests use temporary directories only.
Sorting happens while the directory is read, not afterwards.

- Everything else works on the tree it returns.
- Sizes are taken from the directory entry when the platform allows it.

## Why

The summary line describes what was printed, not what was found.
Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.
