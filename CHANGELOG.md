# Changelog

The public API is one function and two dataclasses.

## Examples

Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.

## Why

Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.

- Everything else works on the tree it returns.
- Colour is decided in a single place so the rest stays testable.

## Caveats

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.

## Design

The counters are collected during the walk and reused for the summary.
The exit code is one when anything failed.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.
