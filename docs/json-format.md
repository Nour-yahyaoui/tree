# Json Format

Tests use temporary directories only.

## Caveats

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.

- Nothing here needs a third party package.
- Sorting happens while the directory is read, not afterwards.

## Design

The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.

## Extensions

A link that would loop is marked instead of followed.
Sizes are taken from the directory entry when the platform allows it.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.

## Overview

Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.

- Nothing here needs a third party package.
- Symlinks are reported with their target.
