# Recipes

The counters are collected during the walk and reused for the summary.

## Examples

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.

- A link that would loop is marked instead of followed.
- The public API is one function and two dataclasses.

## Why

This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.
