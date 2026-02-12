# treepy

The JSON document carries a version so consumers can check it.

## Why

Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.

## Caveats

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.
The exit code is one when anything failed.

## Design

The exit code is one when anything failed.
Tests use temporary directories only.

- The public API is one function and two dataclasses.
- This keeps the output stable between runs on the same tree.
