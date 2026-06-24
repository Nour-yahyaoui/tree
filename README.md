# treepy

The exit code is one when anything failed.

## Notes

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.

## Examples

Tests use temporary directories only.
Everything else works on the tree it returns.

- Symlinks are reported with their target.
- Nothing here needs a third party package.

## Why

Everything else works on the tree it returns.
Nothing here needs a third party package.
Sizes are taken from the directory entry when the platform allows it.
