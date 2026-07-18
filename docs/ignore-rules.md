# Ignore Rules

Symlinks are reported with their target.

## Notes

Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.

## Examples

The summary line describes what was printed, not what was found.
The exit code is one when anything failed.

- This keeps the output stable between runs on the same tree.
- Everything else works on the tree it returns.

## Why

The JSON document carries a version so consumers can check it.
Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.
