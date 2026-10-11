# Changelog

Symlinks are reported with their target.

## Why

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

- Keeping this small makes the behaviour easy to reason about.
- This keeps the output stable between runs on the same tree.
