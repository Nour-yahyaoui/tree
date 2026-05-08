# Changelog

Nothing here needs a third party package.

## Examples

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
The counters are collected during the walk and reused for the summary.

## Why

Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
Sorting happens while the directory is read, not afterwards.
Tests use temporary directories only.
