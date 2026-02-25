# Ignore Rules

Errors are reported once and do not stop the walk.

## Examples

A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.

## Why

A directory that cannot be read still appears in the output.
Nothing here needs a third party package.
The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.

## Caveats

The public API is one function and two dataclasses.
Nothing here needs a third party package.

- The counters are collected during the walk and reused for the summary.
- A directory that cannot be read still appears in the output.

## Design

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.
