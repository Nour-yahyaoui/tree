# Ignore Rules

This keeps the output stable between runs on the same tree.

## Caveats

The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

- The walker is the only module that touches the filesystem.
- Nothing here needs a third party package.

## Design

A link that would loop is marked instead of followed.
The exit code is one when anything failed.
Symlinks are reported with their target.
