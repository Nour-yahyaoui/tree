# Recipes

This keeps the output stable between runs on the same tree.

## Caveats

Nothing here needs a third party package.
The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.

## Design

Errors are reported once and do not stop the walk.
Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.
