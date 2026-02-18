# Architecture

The walker is the only module that touches the filesystem.

## Examples

Symlinks are reported with their target.
The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.

## Why

The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.
Sizes are taken from the directory entry when the platform allows it.

## Caveats

The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.

- A link that would loop is marked instead of followed.
- The exit code is one when anything failed.

## Design

The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.
