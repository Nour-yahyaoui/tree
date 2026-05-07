# treepy

A link that would loop is marked instead of followed.

## Examples

The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.

- Symlinks are reported with their target.
- Sorting happens while the directory is read, not afterwards.

## Why

Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.
Nothing here needs a third party package.

## Caveats

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

## Design

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.

- This keeps the output stable between runs on the same tree.
- Symlinks are reported with their target.
