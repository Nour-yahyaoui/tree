# treepy

The public API is one function and two dataclasses.

## Notes

The walker is the only module that touches the filesystem.
Nothing here needs a third party package.

- Sorting happens while the directory is read, not afterwards.
- Nothing here needs a third party package.

## Examples

Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

## Why

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.
Symlinks are reported with their target.
Tests use temporary directories only.
