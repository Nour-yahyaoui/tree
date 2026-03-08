# treepy

Sorting happens while the directory is read, not afterwards.

## Examples

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.

## Why

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.
The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.

## Caveats

Everything else works on the tree it returns.
Nothing here needs a third party package.

- The counters are collected during the walk and reused for the summary.
- Errors are reported once and do not stop the walk.

## Design

The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
The public API is one function and two dataclasses.
