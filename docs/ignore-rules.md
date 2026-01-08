# Ignore Rules

Patterns are matched against the path relative to the root of the scan.

## Examples

Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.

- Errors are reported once and do not stop the walk.
- The counters are collected during the walk and reused for the summary.

## Why

A directory that cannot be read still appears in the output.
The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.

## Caveats

Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.

## Design

The glyphs are chosen once, when the renderer is built.
The public API is one function and two dataclasses.

- The counters are collected during the walk and reused for the summary.
- Sorting happens while the directory is read, not afterwards.
