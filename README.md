# treepy

The JSON document carries a version so consumers can check it.

## Examples

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.

- The exit code is one when anything failed.
- Nothing here needs a third party package.

## Why

Symlinks are reported with their target.
The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.

## Caveats

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.
Sizes are taken from the directory entry when the platform allows it.

## Design

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.

- Nothing here needs a third party package.
- Keeping this small makes the behaviour easy to reason about.
