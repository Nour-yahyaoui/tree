# Json Format

The walker is the only module that touches the filesystem.

## Examples

Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.
Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.

## Why

The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

- A link that would loop is marked instead of followed.
- Errors are reported once and do not stop the walk.

## Caveats

The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.

## Design

A link that would loop is marked instead of followed.
The public API is one function and two dataclasses.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
