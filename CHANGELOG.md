# Changelog

The counters are collected during the walk and reused for the summary.

## Why

The exit code is one when anything failed.
Everything else works on the tree it returns.
Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.

## Caveats

A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.

- The glyphs are chosen once, when the renderer is built.
- A link that would loop is marked instead of followed.

## Design

Symlinks are reported with their target.
A directory that cannot be read still appears in the output.
Colour is decided in a single place so the rest stays testable.
