# treepy

Errors are reported once and do not stop the walk.

## Examples

The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
Tests use temporary directories only.

## Why

Nothing here needs a third party package.
The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.

## Caveats

Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.

- This keeps the output stable between runs on the same tree.
- The exit code is one when anything failed.

## Design

The summary line describes what was printed, not what was found.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.
