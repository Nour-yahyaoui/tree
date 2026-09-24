# Changelog

Sizes are taken from the directory entry when the platform allows it.

## Design

Symlinks are reported with their target.
The counters are collected during the walk and reused for the summary.
The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.
