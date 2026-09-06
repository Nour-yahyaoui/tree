# Changelog

Sorting happens while the directory is read, not afterwards.

## Why

Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.

## Caveats

Nothing here needs a third party package.
The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
A link that would loop is marked instead of followed.

## Design

The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.

- Patterns are matched against the path relative to the root of the scan.
- Keeping this small makes the behaviour easy to reason about.
