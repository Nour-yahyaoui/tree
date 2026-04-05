# Ignore Rules

The glyphs are chosen once, when the renderer is built.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.

## Notes

This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
Sizes are taken from the directory entry when the platform allows it.
