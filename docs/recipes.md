# Recipes

Everything else works on the tree it returns.

## Caveats

Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
Sizes are taken from the directory entry when the platform allows it.

## Design

The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.

- Sorting happens while the directory is read, not afterwards.
- A link that would loop is marked instead of followed.
