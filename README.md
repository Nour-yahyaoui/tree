# treepy

Sizes are taken from the directory entry when the platform allows it.

## Notes

The exit code is one when anything failed.
A directory that cannot be read still appears in the output.

- A directory that cannot be read still appears in the output.
- This keeps the output stable between runs on the same tree.

## Examples

Errors are reported once and do not stop the walk.
Symlinks are reported with their target.
Nothing here needs a third party package.

## Why

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
