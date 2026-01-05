# treepy

Colour is decided in a single place so the rest stays testable.

## Caveats

Symlinks are reported with their target.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.

## Design

The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.

- Patterns are matched against the path relative to the root of the scan.
- Sorting happens while the directory is read, not afterwards.

## Extensions

A link that would loop is marked instead of followed.
The exit code is one when anything failed.
A directory that cannot be read still appears in the output.

## Overview

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.
