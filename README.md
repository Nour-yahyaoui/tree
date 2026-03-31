# treepy

This keeps the output stable between runs on the same tree.

## Caveats

The summary line describes what was printed, not what was found.
Tests use temporary directories only.

- The counters are collected during the walk and reused for the summary.
- A link that would loop is marked instead of followed.

## Design

Sorting happens while the directory is read, not afterwards.
Nothing here needs a third party package.
Tests use temporary directories only.

## Extensions

The glyphs are chosen once, when the renderer is built.
The counters are collected during the walk and reused for the summary.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

## Overview

This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.

- Everything else works on the tree it returns.
- Keeping this small makes the behaviour easy to reason about.
