# Changelog

The exit code is one when anything failed.

## Caveats

Symlinks are reported with their target.
The public API is one function and two dataclasses.

- The glyphs are chosen once, when the renderer is built.
- Everything else works on the tree it returns.

## Design

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
