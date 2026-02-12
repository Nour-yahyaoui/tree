# treepy

The walker is the only module that touches the filesystem.

## Caveats

Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.

## Design

Colour is decided in a single place so the rest stays testable.
Errors are reported once and do not stop the walk.

- A directory that cannot be read still appears in the output.
- The exit code is one when anything failed.

## Extensions

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.

## Overview

This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
Errors are reported once and do not stop the walk.
Tests use temporary directories only.
