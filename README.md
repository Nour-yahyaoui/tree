# treepy

Sizes are taken from the directory entry when the platform allows it.

## Examples

Patterns are matched against the path relative to the root of the scan.
The public API is one function and two dataclasses.
Sizes are taken from the directory entry when the platform allows it.

## Why

Nothing here needs a third party package.
The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.
The public API is one function and two dataclasses.

## Caveats

The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.

- The counters are collected during the walk and reused for the summary.
- Colour is decided in a single place so the rest stays testable.

## Design

The glyphs are chosen once, when the renderer is built.
Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.
