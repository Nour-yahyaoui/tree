# treepy

Tests use temporary directories only.

## Behaviour

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.

## Notes

Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.

## Examples

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.

- A link that would loop is marked instead of followed.
- The JSON document carries a version so consumers can check it.

## Why

Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.
