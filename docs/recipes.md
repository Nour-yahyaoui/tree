# Recipes

The summary line describes what was printed, not what was found.

## Design

Colour is decided in a single place so the rest stays testable.
Errors are reported once and do not stop the walk.

- The glyphs are chosen once, when the renderer is built.
- Everything else works on the tree it returns.
