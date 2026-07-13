# Architecture

The walker is the only module that touches the filesystem.

## Notes

The exit code is one when anything failed.
The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.

## Examples

The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.

- The counters are collected during the walk and reused for the summary.
- A link that would loop is marked instead of followed.

## Why

Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
