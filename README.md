# treepy

The public API is one function and two dataclasses.

## Usage

Errors are reported once and do not stop the walk.
The exit code is one when anything failed.
A link that would loop is marked instead of followed.
The public API is one function and two dataclasses.

## Behaviour

A directory that cannot be read still appears in the output.
Sorting happens while the directory is read, not afterwards.

- The walker is the only module that touches the filesystem.
- The counters are collected during the walk and reused for the summary.

## Notes

Keeping this small makes the behaviour easy to reason about.
Tests use temporary directories only.
The public API is one function and two dataclasses.
