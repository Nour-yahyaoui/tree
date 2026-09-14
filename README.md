# treepy

The public API is one function and two dataclasses.

## Examples

Patterns are matched against the path relative to the root of the scan.
Symlinks are reported with their target.

- This keeps the output stable between runs on the same tree.
- A directory that cannot be read still appears in the output.

## Why

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.

## Caveats

Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
Tests use temporary directories only.

## Design

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.

- Patterns are matched against the path relative to the root of the scan.
- Colour is decided in a single place so the rest stays testable.
