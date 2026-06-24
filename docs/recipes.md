# Recipes

A link that would loop is marked instead of followed.

## Details

This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.
Tests use temporary directories only.
Keeping this small makes the behaviour easy to reason about.

## Usage

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.

- Colour is decided in a single place so the rest stays testable.
- The walker is the only module that touches the filesystem.

## Behaviour

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.

## Notes

Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
Tests use temporary directories only.
The summary line describes what was printed, not what was found.
