# Changelog

Patterns are matched against the path relative to the root of the scan.

## Examples

A directory that cannot be read still appears in the output.
Sorting happens while the directory is read, not afterwards.

- The JSON document carries a version so consumers can check it.
- Sorting happens while the directory is read, not afterwards.

## Why

A link that would loop is marked instead of followed.
Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
