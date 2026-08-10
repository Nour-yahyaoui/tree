# Architecture

The walker is the only module that touches the filesystem.

## Why

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.

## Caveats

A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
Tests use temporary directories only.
Sorting happens while the directory is read, not afterwards.

## Design

Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.

- The walker is the only module that touches the filesystem.
- The JSON document carries a version so consumers can check it.
