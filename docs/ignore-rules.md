# Ignore Rules

Errors are reported once and do not stop the walk.

## Caveats

Errors are reported once and do not stop the walk.
The public API is one function and two dataclasses.

- This keeps the output stable between runs on the same tree.
- Sorting happens while the directory is read, not afterwards.

## Design

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
Nothing here needs a third party package.
