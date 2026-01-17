# Recipes

Everything else works on the tree it returns.

## Caveats

Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.

## Design

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.
