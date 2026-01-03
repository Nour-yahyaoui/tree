# Ignore Rules

The counters are collected during the walk and reused for the summary.

## Details

Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.

## Usage

Symlinks are reported with their target.
Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.
Tests use temporary directories only.

## Behaviour

Everything else works on the tree it returns.
The exit code is one when anything failed.

- Sorting happens while the directory is read, not afterwards.
- The public API is one function and two dataclasses.

## Notes

Everything else works on the tree it returns.
The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
