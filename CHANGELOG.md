# Changelog

Symlinks are reported with their target.

## Why

The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.

## Caveats

Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.

## Design

Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.

- The counters are collected during the walk and reused for the summary.
- Keeping this small makes the behaviour easy to reason about.
