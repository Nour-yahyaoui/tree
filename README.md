# treepy

A link that would loop is marked instead of followed.

## Caveats

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.

- Sorting happens while the directory is read, not afterwards.
- A link that would loop is marked instead of followed.

## Design

Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
Keeping this small makes the behaviour easy to reason about.

## Extensions

Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.
The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.

## Overview

Patterns are matched against the path relative to the root of the scan.
Symlinks are reported with their target.

- Everything else works on the tree it returns.
- Sorting happens while the directory is read, not afterwards.
