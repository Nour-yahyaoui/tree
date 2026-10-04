# Recipes

Patterns are matched against the path relative to the root of the scan.

## Examples

Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.
Errors are reported once and do not stop the walk.

## Why

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.

- The glyphs are chosen once, when the renderer is built.
- Nothing here needs a third party package.

## Caveats

Colour is decided in a single place so the rest stays testable.
Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.

## Design

The public API is one function and two dataclasses.
The exit code is one when anything failed.
Symlinks are reported with their target.
The summary line describes what was printed, not what was found.
