# treepy

Colour is decided in a single place so the rest stays testable.

## Why

Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.

## Caveats

Tests use temporary directories only.
Colour is decided in a single place so the rest stays testable.
The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.

## Design

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.

- Everything else works on the tree it returns.
- The summary line describes what was printed, not what was found.
