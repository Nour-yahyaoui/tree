# treepy

Sorting happens while the directory is read, not afterwards.

## Details

The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.

- Errors are reported once and do not stop the walk.
- The walker is the only module that touches the filesystem.

## Usage

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.

## Behaviour

The exit code is one when anything failed.
Tests use temporary directories only.
The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.

## Notes

Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.

- Sizes are taken from the directory entry when the platform allows it.
- The counters are collected during the walk and reused for the summary.
