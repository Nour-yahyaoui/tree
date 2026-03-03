# Performance

Sizes are taken from the directory entry when the platform allows it.

## Usage

The JSON document carries a version so consumers can check it.
Tests use temporary directories only.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

## Behaviour

Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.

- The walker is the only module that touches the filesystem.
- The JSON document carries a version so consumers can check it.

## Notes

Keeping this small makes the behaviour easy to reason about.
Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.
