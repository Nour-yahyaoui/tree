# treepy

Symlinks are reported with their target.

## Notes

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.

## Examples

Nothing here needs a third party package.
Tests use temporary directories only.

- The counters are collected during the walk and reused for the summary.
- The glyphs are chosen once, when the renderer is built.

## Why

Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.
Nothing here needs a third party package.
