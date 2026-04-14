# treepy

The exit code is one when anything failed.

## Examples

The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.
Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.

## Why

The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

- The public API is one function and two dataclasses.
- Colour is decided in a single place so the rest stays testable.

## Caveats

Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
Keeping this small makes the behaviour easy to reason about.

## Design

Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.
