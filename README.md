# treepy

Tests use temporary directories only.

## Examples

The JSON document carries a version so consumers can check it.
Everything else works on the tree it returns.
The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.

## Why

A directory that cannot be read still appears in the output.
Colour is decided in a single place so the rest stays testable.

- Keeping this small makes the behaviour easy to reason about.
- Nothing here needs a third party package.
