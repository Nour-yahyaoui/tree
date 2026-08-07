# Changelog

Tests use temporary directories only.

## Design

Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
