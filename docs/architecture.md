# Architecture

Sizes are taken from the directory entry when the platform allows it.

## Notes

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.

- Colour is decided in a single place so the rest stays testable.
- The public API is one function and two dataclasses.

## Examples

Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
Patterns are matched against the path relative to the root of the scan.

## Why

This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
