# Changelog

A link that would loop is marked instead of followed.

## Behaviour

Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.

- The counters are collected during the walk and reused for the summary.
- Nothing here needs a third party package.

## Notes

Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.

## Examples

The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.

## Why

The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.

- The summary line describes what was printed, not what was found.
- Sorting happens while the directory is read, not afterwards.
