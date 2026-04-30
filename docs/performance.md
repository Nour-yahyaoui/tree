# Performance

Patterns are matched against the path relative to the root of the scan.

## Why

Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.

- Patterns are matched against the path relative to the root of the scan.
- This keeps the output stable between runs on the same tree.

## Caveats

The summary line describes what was printed, not what was found.
Nothing here needs a third party package.
The exit code is one when anything failed.

## Design

A directory that cannot be read still appears in the output.
The exit code is one when anything failed.
Tests use temporary directories only.
This keeps the output stable between runs on the same tree.
