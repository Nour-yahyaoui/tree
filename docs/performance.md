# Performance

Colour is decided in a single place so the rest stays testable.

## Why

Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.

- A directory that cannot be read still appears in the output.
- Everything else works on the tree it returns.
