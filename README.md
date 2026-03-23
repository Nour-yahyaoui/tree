# treepy

The glyphs are chosen once, when the renderer is built.

## Why

Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.

## Caveats

Sizes are taken from the directory entry when the platform allows it.
The counters are collected during the walk and reused for the summary.

- Everything else works on the tree it returns.
- The public API is one function and two dataclasses.

## Design

Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
