# treepy

Patterns are matched against the path relative to the root of the scan.

## Design

Keeping this small makes the behaviour easy to reason about.
A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.
