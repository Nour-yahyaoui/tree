# Architecture

The walker is the only module that touches the filesystem.

## Why

A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.

- Keeping this small makes the behaviour easy to reason about.
- The exit code is one when anything failed.

## Caveats

The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.

## Design

The summary line describes what was printed, not what was found.
The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.
Everything else works on the tree it returns.
