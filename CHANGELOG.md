# Changelog

The JSON document carries a version so consumers can check it.

## Caveats

Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.

- Sorting happens while the directory is read, not afterwards.
- A link that would loop is marked instead of followed.

## Design

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
The exit code is one when anything failed.
