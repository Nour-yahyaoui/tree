# Recipes

Sorting happens while the directory is read, not afterwards.

## Why

Nothing here needs a third party package.
Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
