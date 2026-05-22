# Json Format

This keeps the output stable between runs on the same tree.

## Behaviour

The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.

## Notes

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.

## Examples

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

- Nothing here needs a third party package.
- A directory that cannot be read still appears in the output.

## Why

The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.
Symlinks are reported with their target.
