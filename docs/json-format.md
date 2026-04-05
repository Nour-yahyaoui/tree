# Json Format

The summary line describes what was printed, not what was found.

## Examples

A link that would loop is marked instead of followed.
The summary line describes what was printed, not what was found.

- A link that would loop is marked instead of followed.
- Sizes are taken from the directory entry when the platform allows it.

## Why

Tests use temporary directories only.
The walker is the only module that touches the filesystem.
Symlinks are reported with their target.

## Caveats

Tests use temporary directories only.
The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.

## Design

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.

- The summary line describes what was printed, not what was found.
- Sizes are taken from the directory entry when the platform allows it.
