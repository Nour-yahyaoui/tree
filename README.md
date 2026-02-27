# treepy

Patterns are matched against the path relative to the root of the scan.

## Usage

Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.

- Errors are reported once and do not stop the walk.
- Keeping this small makes the behaviour easy to reason about.
