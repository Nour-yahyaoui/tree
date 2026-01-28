# Recipes

This keeps the output stable between runs on the same tree.

## Caveats

A directory that cannot be read still appears in the output.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

## Design

The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.
