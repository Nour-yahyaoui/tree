# treepy

The walker is the only module that touches the filesystem.

## Notes

The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
The summary line describes what was printed, not what was found.

## Examples

Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.

## Why

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.

- The summary line describes what was printed, not what was found.
- Patterns are matched against the path relative to the root of the scan.
