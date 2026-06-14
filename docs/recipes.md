# Recipes

A link that would loop is marked instead of followed.

## Examples

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.
Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.

## Why

The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.

- The JSON document carries a version so consumers can check it.
- Errors are reported once and do not stop the walk.

## Caveats

Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.

## Design

Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.
The counters are collected during the walk and reused for the summary.
Errors are reported once and do not stop the walk.
