# Recipes

The counters are collected during the walk and reused for the summary.

## Design

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.
