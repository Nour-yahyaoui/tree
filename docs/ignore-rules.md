# Ignore Rules

Symlinks are reported with their target.

## Examples

The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.
The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.

## Why

Colour is decided in a single place so the rest stays testable.
Patterns are matched against the path relative to the root of the scan.

- The counters are collected during the walk and reused for the summary.
- Sizes are taken from the directory entry when the platform allows it.

## Caveats

Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.
Tests use temporary directories only.

## Design

Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.
