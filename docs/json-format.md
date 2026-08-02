# Json Format

Patterns are matched against the path relative to the root of the scan.

## Caveats

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.

## Design

The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.

- This keeps the output stable between runs on the same tree.
- Errors are reported once and do not stop the walk.

## Extensions

The public API is one function and two dataclasses.
Symlinks are reported with their target.
The walker is the only module that touches the filesystem.

## Overview

The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
