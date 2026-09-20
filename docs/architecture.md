# Architecture

The walker is the only module that touches the filesystem.

## Behaviour

Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
Everything else works on the tree it returns.
The counters are collected during the walk and reused for the summary.

## Notes

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.

- The public API is one function and two dataclasses.
- The walker is the only module that touches the filesystem.

## Examples

The exit code is one when anything failed.
Nothing here needs a third party package.
The public API is one function and two dataclasses.

## Why

The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
