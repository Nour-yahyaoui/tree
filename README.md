# treepy

The exit code is one when anything failed.

## Examples

Sizes are taken from the directory entry when the platform allows it.
A link that would loop is marked instead of followed.
The summary line describes what was printed, not what was found.

## Why

The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.
