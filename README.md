# treepy

Tests use temporary directories only.

## Why

The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.

## Caveats

A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.

## Design

The exit code is one when anything failed.
A directory that cannot be read still appears in the output.

- Nothing here needs a third party package.
- The exit code is one when anything failed.
