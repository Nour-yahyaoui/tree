# Json Format

Sizes are taken from the directory entry when the platform allows it.

## Caveats

Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.

## Design

Everything else works on the tree it returns.
Nothing here needs a third party package.
Symlinks are reported with their target.
A directory that cannot be read still appears in the output.

## Extensions

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.

- The glyphs are chosen once, when the renderer is built.
- The exit code is one when anything failed.

## Overview

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
