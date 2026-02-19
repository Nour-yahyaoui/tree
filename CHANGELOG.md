# Changelog

Sizes are taken from the directory entry when the platform allows it.

## Examples

The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.

## Why

Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.

- Patterns are matched against the path relative to the root of the scan.
- A directory that cannot be read still appears in the output.
