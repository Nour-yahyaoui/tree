# Performance

Patterns are matched against the path relative to the root of the scan.

## Examples

The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.

## Why

The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.
