# Recipes

The walker is the only module that touches the filesystem.

## Behaviour

Errors are reported once and do not stop the walk.
Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.

## Notes

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.

- The public API is one function and two dataclasses.
- Nothing here needs a third party package.

## Examples

The counters are collected during the walk and reused for the summary.
Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.

## Why

The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
Errors are reported once and do not stop the walk.
The walker is the only module that touches the filesystem.
