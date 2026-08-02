# Architecture

The summary line describes what was printed, not what was found.

## Examples

Tests use temporary directories only.
This keeps the output stable between runs on the same tree.

- The exit code is one when anything failed.
- Nothing here needs a third party package.

## Why

Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
