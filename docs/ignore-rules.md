# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Design

Sorting happens while the directory is read, not afterwards.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Extensions

The public API is one function and two dataclasses.
Nothing here needs a third party package.
Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.

## Overview

The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.

- Patterns are matched against the path relative to the root of the scan.
- This keeps the output stable between runs on the same tree.
