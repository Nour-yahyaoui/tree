# Architecture

Errors are reported once and do not stop the walk.

## Behaviour

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Sizes are taken from the directory entry when the platform allows it.
The exit code is one when anything failed.

## Notes

Patterns are matched against the path relative to the root of the scan.
Symlinks are reported with their target.

- Everything else works on the tree it returns.
- The walker is the only module that touches the filesystem.

## Examples

Tests use temporary directories only.
Symlinks are reported with their target.
The summary line describes what was printed, not what was found.

## Why

Tests use temporary directories only.
The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
This keeps the output stable between runs on the same tree.
