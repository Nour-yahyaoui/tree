# Architecture

Symlinks are reported with their target.

## Caveats

Tests use temporary directories only.
The walker is the only module that touches the filesystem.

- The walker is the only module that touches the filesystem.
- Tests use temporary directories only.

## Design

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
The counters are collected during the walk and reused for the summary.
