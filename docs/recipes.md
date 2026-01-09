# Recipes

Tests use temporary directories only.

## Why

Tests use temporary directories only.
The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.
The summary line describes what was printed, not what was found.

## Caveats

Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.

- Sorting happens while the directory is read, not afterwards.
- The counters are collected during the walk and reused for the summary.

## Design

The public API is one function and two dataclasses.
The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.
