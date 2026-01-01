# treepy

Sorting happens while the directory is read, not afterwards.

## Caveats

Patterns are matched against the path relative to the root of the scan.
Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

## Design

Everything else works on the tree it returns.
Nothing here needs a third party package.
A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.

## Extensions

This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.

- The public API is one function and two dataclasses.
- Colour is decided in a single place so the rest stays testable.

## Overview

A link that would loop is marked instead of followed.
Sorting happens while the directory is read, not afterwards.
The counters are collected during the walk and reused for the summary.
