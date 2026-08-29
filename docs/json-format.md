# Json Format

Errors are reported once and do not stop the walk.

## Examples

Patterns are matched against the path relative to the root of the scan.
Tests use temporary directories only.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

## Why

The JSON document carries a version so consumers can check it.
The counters are collected during the walk and reused for the summary.

- The public API is one function and two dataclasses.
- A link that would loop is marked instead of followed.

## Caveats

The glyphs are chosen once, when the renderer is built.
The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.

## Design

This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
The exit code is one when anything failed.
