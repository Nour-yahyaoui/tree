# Architecture

This keeps the output stable between runs on the same tree.

## Behaviour

Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.

## Notes

Nothing here needs a third party package.
Keeping this small makes the behaviour easy to reason about.

- This keeps the output stable between runs on the same tree.
- Nothing here needs a third party package.

## Examples

The exit code is one when anything failed.
Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.

## Why

A directory that cannot be read still appears in the output.
The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.
Tests use temporary directories only.
