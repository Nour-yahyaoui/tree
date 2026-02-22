# Changelog

Keeping this small makes the behaviour easy to reason about.

## Examples

Nothing here needs a third party package.
A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.

## Why

This keeps the output stable between runs on the same tree.
Everything else works on the tree it returns.

- The counters are collected during the walk and reused for the summary.
- Symlinks are reported with their target.

## Caveats

Everything else works on the tree it returns.
Symlinks are reported with their target.
A directory that cannot be read still appears in the output.

## Design

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.
The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
