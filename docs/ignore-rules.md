# Ignore Rules

The counters are collected during the walk and reused for the summary.

## Details

The summary line describes what was printed, not what was found.
The counters are collected during the walk and reused for the summary.
Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.

## Usage

Symlinks are reported with their target.
Errors are reported once and do not stop the walk.

- The walker is the only module that touches the filesystem.
- The public API is one function and two dataclasses.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.
Errors are reported once and do not stop the walk.

## Notes

Errors are reported once and do not stop the walk.
The summary line describes what was printed, not what was found.
The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
