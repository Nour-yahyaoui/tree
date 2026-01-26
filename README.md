# treepy

Sizes are taken from the directory entry when the platform allows it.

## Behaviour

Nothing here needs a third party package.
The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.

## Notes

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.

- The walker is the only module that touches the filesystem.
- A link that would loop is marked instead of followed.

## Examples

The glyphs are chosen once, when the renderer is built.
The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.

## Why

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.
Symlinks are reported with their target.
