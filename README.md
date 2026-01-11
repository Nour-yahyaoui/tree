# treepy

Patterns are matched against the path relative to the root of the scan.

## Examples

A link that would loop is marked instead of followed.
The exit code is one when anything failed.

- A link that would loop is marked instead of followed.
- Sorting happens while the directory is read, not afterwards.

## Why

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.
