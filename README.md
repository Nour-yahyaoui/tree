# treepy

Patterns are matched against the path relative to the root of the scan.

## Why

Everything else works on the tree it returns.
Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.

## Caveats

This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.

## Design

The summary line describes what was printed, not what was found.
Nothing here needs a third party package.

- A link that would loop is marked instead of followed.
- Errors are reported once and do not stop the walk.
