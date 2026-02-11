# treepy

A directory that cannot be read still appears in the output.

## Behaviour

The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.

## Notes

The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.
The counters are collected during the walk and reused for the summary.
The exit code is one when anything failed.

## Examples

The exit code is one when anything failed.
The summary line describes what was printed, not what was found.

- The summary line describes what was printed, not what was found.
- The counters are collected during the walk and reused for the summary.

## Why

Tests use temporary directories only.
Nothing here needs a third party package.
The JSON document carries a version so consumers can check it.
