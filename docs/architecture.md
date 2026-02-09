# Architecture

This keeps the output stable between runs on the same tree.

## Examples

Errors are reported once and do not stop the walk.
The walker is the only module that touches the filesystem.
Tests use temporary directories only.

## Why

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.
