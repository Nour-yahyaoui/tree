# treepy

The counters are collected during the walk and reused for the summary.

## Why

Tests use temporary directories only.
Sizes are taken from the directory entry when the platform allows it.

- Symlinks are reported with their target.
- The public API is one function and two dataclasses.

## Caveats

The glyphs are chosen once, when the renderer is built.
Tests use temporary directories only.
A directory that cannot be read still appears in the output.

## Design

The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
