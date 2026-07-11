# Architecture

The JSON document carries a version so consumers can check it.

## Notes

This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.

- The walker is the only module that touches the filesystem.
- The walker is the only module that touches the filesystem.

## Examples

Errors are reported once and do not stop the walk.
Sorting happens while the directory is read, not afterwards.
The exit code is one when anything failed.

## Why

A link that would loop is marked instead of followed.
Keeping this small makes the behaviour easy to reason about.
The glyphs are chosen once, when the renderer is built.
Patterns are matched against the path relative to the root of the scan.
