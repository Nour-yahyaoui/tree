# Recipes

The public API is one function and two dataclasses.

## Examples

Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.

- Sorting happens while the directory is read, not afterwards.
- Symlinks are reported with their target.

## Why

The summary line describes what was printed, not what was found.
The exit code is one when anything failed.
Nothing here needs a third party package.

## Caveats

Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Design

This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.

- The walker is the only module that touches the filesystem.
- Nothing here needs a third party package.
