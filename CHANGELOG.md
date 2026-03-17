# Changelog

Tests use temporary directories only.

## Notes

Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.
This keeps the output stable between runs on the same tree.

## Examples

The public API is one function and two dataclasses.
The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.
A directory that cannot be read still appears in the output.

## Why

Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.

- Colour is decided in a single place so the rest stays testable.
- The public API is one function and two dataclasses.
