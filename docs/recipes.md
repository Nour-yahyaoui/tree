# Recipes

Keeping this small makes the behaviour easy to reason about.

## Caveats

The exit code is one when anything failed.
Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

## Design

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

- The glyphs are chosen once, when the renderer is built.
- Tests use temporary directories only.
