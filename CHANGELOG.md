# Changelog

The JSON document carries a version so consumers can check it.

## Behaviour

The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.

- Everything else works on the tree it returns.
- Colour is decided in a single place so the rest stays testable.

## Notes

Sorting happens while the directory is read, not afterwards.
The exit code is one when anything failed.
Tests use temporary directories only.

## Examples

Colour is decided in a single place so the rest stays testable.
The summary line describes what was printed, not what was found.
Errors are reported once and do not stop the walk.
The counters are collected during the walk and reused for the summary.

## Why

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.

- The counters are collected during the walk and reused for the summary.
- Errors are reported once and do not stop the walk.
