# Changelog

Colour is decided in a single place so the rest stays testable.

## Behaviour

This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.
Sizes are taken from the directory entry when the platform allows it.

## Notes

The glyphs are chosen once, when the renderer is built.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.

## Examples

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.

- The public API is one function and two dataclasses.
- Errors are reported once and do not stop the walk.

## Why

A link that would loop is marked instead of followed.
The exit code is one when anything failed.
Everything else works on the tree it returns.
