# Architecture

The walker is the only module that touches the filesystem.

## Caveats

Errors are reported once and do not stop the walk.
Sorting happens while the directory is read, not afterwards.

- The JSON document carries a version so consumers can check it.
- Nothing here needs a third party package.

## Design

A link that would loop is marked instead of followed.
Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.
