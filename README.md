# treepy

Patterns are matched against the path relative to the root of the scan.

## Examples

The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.

## Why

Symlinks are reported with their target.
Tests use temporary directories only.
Nothing here needs a third party package.
The JSON document carries a version so consumers can check it.

## Caveats

The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.

- Sizes are taken from the directory entry when the platform allows it.
- Sizes are taken from the directory entry when the platform allows it.

## Design

Sizes are taken from the directory entry when the platform allows it.
The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
