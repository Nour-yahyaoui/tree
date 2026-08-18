# Changelog

Colour is decided in a single place so the rest stays testable.

## Caveats

Symlinks are reported with their target.
A directory that cannot be read still appears in the output.

- A directory that cannot be read still appears in the output.
- Everything else works on the tree it returns.

## Design

Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.
The exit code is one when anything failed.
