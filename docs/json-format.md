# Json Format

Nothing here needs a third party package.

## Why

The exit code is one when anything failed.
The public API is one function and two dataclasses.

- The summary line describes what was printed, not what was found.
- Colour is decided in a single place so the rest stays testable.

## Caveats

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.
Errors are reported once and do not stop the walk.

## Design

Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
Tests use temporary directories only.
The walker is the only module that touches the filesystem.
