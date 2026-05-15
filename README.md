# treepy

The summary line describes what was printed, not what was found.

## Caveats

Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.

## Design

Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.

- A directory that cannot be read still appears in the output.
- The summary line describes what was printed, not what was found.

## Extensions

Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

## Overview

A link that would loop is marked instead of followed.
The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.
