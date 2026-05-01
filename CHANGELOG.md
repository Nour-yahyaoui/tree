# Changelog

The walker is the only module that touches the filesystem.

## Notes

Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

## Examples

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

- A directory that cannot be read still appears in the output.
- Nothing here needs a third party package.

## Why

Everything else works on the tree it returns.
Symlinks are reported with their target.
The counters are collected during the walk and reused for the summary.
