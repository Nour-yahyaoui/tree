# Architecture

Colour is decided in a single place so the rest stays testable.

## Examples

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

## Why

The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.

## Caveats

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.

- The public API is one function and two dataclasses.
- The JSON document carries a version so consumers can check it.

## Design

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
