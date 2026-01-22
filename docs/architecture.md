# Architecture

The JSON document carries a version so consumers can check it.

## Details

Errors are reported once and do not stop the walk.
Tests use temporary directories only.
Everything else works on the tree it returns.

## Usage

Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.
The walker is the only module that touches the filesystem.

## Behaviour

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.

- Keeping this small makes the behaviour easy to reason about.
- A link that would loop is marked instead of followed.

## Notes

The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
Errors are reported once and do not stop the walk.
