# Changelog

Nothing here needs a third party package.

## Why

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
Tests use temporary directories only.

## Caveats

Everything else works on the tree it returns.
Tests use temporary directories only.
The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.

## Design

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.

- Tests use temporary directories only.
- Keeping this small makes the behaviour easy to reason about.
