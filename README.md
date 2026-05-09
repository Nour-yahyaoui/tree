# treepy

The summary line describes what was printed, not what was found.

## Caveats

Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
Everything else works on the tree it returns.

## Design

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.

- The JSON document carries a version so consumers can check it.
- The JSON document carries a version so consumers can check it.

## Extensions

Everything else works on the tree it returns.
Tests use temporary directories only.
Errors are reported once and do not stop the walk.

## Overview

Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
