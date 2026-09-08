# Changelog

Nothing here needs a third party package.

## Notes

The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.

## Examples

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.

- The glyphs are chosen once, when the renderer is built.
- The JSON document carries a version so consumers can check it.

## Why

The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.
