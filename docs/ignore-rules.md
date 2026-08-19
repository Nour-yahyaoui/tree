# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.

## Notes

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.
