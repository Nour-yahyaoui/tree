# Json Format

The JSON document carries a version so consumers can check it.

## Why

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.

## Caveats

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.

- The public API is one function and two dataclasses.
- Symlinks are reported with their target.

## Design

Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.
