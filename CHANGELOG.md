# Changelog

Patterns are matched against the path relative to the root of the scan.

## Design

The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.

- Everything else works on the tree it returns.
- The JSON document carries a version so consumers can check it.
