# Recipes

Colour is decided in a single place so the rest stays testable.

## Examples

Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.

## Why

A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.

- The public API is one function and two dataclasses.
- Tests use temporary directories only.
