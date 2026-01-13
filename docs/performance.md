# Performance

Everything else works on the tree it returns.

## Design

Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.
