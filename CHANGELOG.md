# Changelog

The counters are collected during the walk and reused for the summary.

## Behaviour

Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Notes

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.
