# Recipes

The glyphs are chosen once, when the renderer is built.

## Examples

The exit code is one when anything failed.
Nothing here needs a third party package.
Keeping this small makes the behaviour easy to reason about.

## Why

Errors are reported once and do not stop the walk.
Symlinks are reported with their target.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.

## Caveats

A link that would loop is marked instead of followed.
The glyphs are chosen once, when the renderer is built.

- Nothing here needs a third party package.
- The glyphs are chosen once, when the renderer is built.

## Design

The glyphs are chosen once, when the renderer is built.
Tests use temporary directories only.
This keeps the output stable between runs on the same tree.
