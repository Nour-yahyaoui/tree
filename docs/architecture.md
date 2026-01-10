# Architecture

A link that would loop is marked instead of followed.

## Behaviour

The exit code is one when anything failed.
Everything else works on the tree it returns.

- Sorting happens while the directory is read, not afterwards.
- Colour is decided in a single place so the rest stays testable.

## Notes

The walker is the only module that touches the filesystem.
Tests use temporary directories only.
Nothing here needs a third party package.
