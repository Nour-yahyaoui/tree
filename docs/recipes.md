# Recipes

The glyphs are chosen once, when the renderer is built.

## Usage

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.

## Behaviour

Everything else works on the tree it returns.
A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
Symlinks are reported with their target.

## Notes

The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.

- Patterns are matched against the path relative to the root of the scan.
- The JSON document carries a version so consumers can check it.
