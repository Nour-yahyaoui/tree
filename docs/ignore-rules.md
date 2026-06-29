# Ignore Rules

A link that would loop is marked instead of followed.

## Why

Patterns are matched against the path relative to the root of the scan.
Everything else works on the tree it returns.

- The JSON document carries a version so consumers can check it.
- Colour is decided in a single place so the rest stays testable.

## Caveats

The counters are collected during the walk and reused for the summary.
The exit code is one when anything failed.
The public API is one function and two dataclasses.

## Design

The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.
