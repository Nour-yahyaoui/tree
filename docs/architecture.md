# Architecture

The exit code is one when anything failed.

## Examples

The summary line describes what was printed, not what was found.
Patterns are matched against the path relative to the root of the scan.
Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.

## Why

The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.

- The exit code is one when anything failed.
- The summary line describes what was printed, not what was found.

## Caveats

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.

## Design

The exit code is one when anything failed.
A link that would loop is marked instead of followed.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.
