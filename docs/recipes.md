# Recipes

Colour is decided in a single place so the rest stays testable.

## Examples

Sorting happens while the directory is read, not afterwards.
Nothing here needs a third party package.
Keeping this small makes the behaviour easy to reason about.

## Why

Sizes are taken from the directory entry when the platform allows it.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
