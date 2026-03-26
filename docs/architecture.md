# Architecture

The summary line describes what was printed, not what was found.

## Behaviour

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.
Tests use temporary directories only.
Errors are reported once and do not stop the walk.

## Notes

Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.

- The glyphs are chosen once, when the renderer is built.
- A link that would loop is marked instead of followed.
