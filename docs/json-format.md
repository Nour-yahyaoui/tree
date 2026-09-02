# Json Format

Patterns are matched against the path relative to the root of the scan.

## Notes

Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.

## Examples

Sorting happens while the directory is read, not afterwards.
A directory that cannot be read still appears in the output.

- Symlinks are reported with their target.
- The walker is the only module that touches the filesystem.

## Why

The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
Sorting happens while the directory is read, not afterwards.
