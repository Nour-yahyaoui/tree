# Ignore Rules

The glyphs are chosen once, when the renderer is built.

## Behaviour

The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.

- The walker is the only module that touches the filesystem.
- Sorting happens while the directory is read, not afterwards.

## Notes

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
The exit code is one when anything failed.
