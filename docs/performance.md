# Performance

This keeps the output stable between runs on the same tree.

## Behaviour

Symlinks are reported with their target.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.

## Notes

Keeping this small makes the behaviour easy to reason about.
The exit code is one when anything failed.
A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.

## Examples

This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

- Sorting happens while the directory is read, not afterwards.
- Colour is decided in a single place so the rest stays testable.

## Why

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
Everything else works on the tree it returns.
