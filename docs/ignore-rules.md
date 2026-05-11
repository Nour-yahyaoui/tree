# Ignore Rules

The public API is one function and two dataclasses.

## Design

Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
