# treepy

A link that would loop is marked instead of followed.

## Caveats

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.

## Design

Everything else works on the tree it returns.
Patterns are matched against the path relative to the root of the scan.

- Symlinks are reported with their target.
- The JSON document carries a version so consumers can check it.

## Extensions

The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.

## Overview

A link that would loop is marked instead of followed.
The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.
