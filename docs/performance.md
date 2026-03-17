# Performance

Colour is decided in a single place so the rest stays testable.

## Details

The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.
Errors are reported once and do not stop the walk.

## Usage

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.

## Behaviour

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.

- Nothing here needs a third party package.
- The counters are collected during the walk and reused for the summary.

## Notes

The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.
