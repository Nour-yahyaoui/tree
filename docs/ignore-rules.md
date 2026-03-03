# Ignore Rules

The public API is one function and two dataclasses.

## Behaviour

Errors are reported once and do not stop the walk.
The walker is the only module that touches the filesystem.

- The summary line describes what was printed, not what was found.
- Sorting happens while the directory is read, not afterwards.

## Notes

Sizes are taken from the directory entry when the platform allows it.
Tests use temporary directories only.
The counters are collected during the walk and reused for the summary.

## Examples

A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
Symlinks are reported with their target.

## Why

Nothing here needs a third party package.
The exit code is one when anything failed.

- Everything else works on the tree it returns.
- The JSON document carries a version so consumers can check it.
