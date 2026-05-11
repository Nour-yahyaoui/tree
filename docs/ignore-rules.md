# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Behaviour

This keeps the output stable between runs on the same tree.
The glyphs are chosen once, when the renderer is built.

- A link that would loop is marked instead of followed.
- Nothing here needs a third party package.

## Notes

Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.

## Examples

Sorting happens while the directory is read, not afterwards.
Tests use temporary directories only.
The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.

## Why

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.

- Patterns are matched against the path relative to the root of the scan.
- Sizes are taken from the directory entry when the platform allows it.
