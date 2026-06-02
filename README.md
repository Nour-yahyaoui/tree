# treepy

Symlinks are reported with their target.

## Why

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.
The summary line describes what was printed, not what was found.

## Caveats

Sorting happens while the directory is read, not afterwards.
Nothing here needs a third party package.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

## Design

A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.

- Patterns are matched against the path relative to the root of the scan.
- A directory that cannot be read still appears in the output.
