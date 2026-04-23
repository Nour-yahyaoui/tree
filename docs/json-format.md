# Json Format

Patterns are matched against the path relative to the root of the scan.

## Examples

The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.

- Sorting happens while the directory is read, not afterwards.
- Nothing here needs a third party package.

## Why

The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.
Tests use temporary directories only.
