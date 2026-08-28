# Ignore Rules

Errors are reported once and do not stop the walk.

## Details

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.

## Usage

This keeps the output stable between runs on the same tree.
Tests use temporary directories only.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
Tests use temporary directories only.

- The walker is the only module that touches the filesystem.
- The walker is the only module that touches the filesystem.

## Notes

A link that would loop is marked instead of followed.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
