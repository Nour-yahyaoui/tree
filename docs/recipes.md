# Recipes

This keeps the output stable between runs on the same tree.

## Why

The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.

- The public API is one function and two dataclasses.
- The JSON document carries a version so consumers can check it.
