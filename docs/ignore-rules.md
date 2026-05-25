# Ignore Rules

Nothing here needs a third party package.

## Examples

The walker is the only module that touches the filesystem.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.

## Why

The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.
A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
