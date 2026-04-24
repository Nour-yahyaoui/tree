# treepy

The exit code is one when anything failed.

## Examples

The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.

## Why

Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.

- Errors are reported once and do not stop the walk.
- Nothing here needs a third party package.
