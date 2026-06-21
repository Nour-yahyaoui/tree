# Json Format

The walker is the only module that touches the filesystem.

## Examples

Errors are reported once and do not stop the walk.
The exit code is one when anything failed.
Symlinks are reported with their target.
The summary line describes what was printed, not what was found.

## Why

Everything else works on the tree it returns.
Nothing here needs a third party package.

- This keeps the output stable between runs on the same tree.
- The walker is the only module that touches the filesystem.

## Caveats

Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.

## Design

The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.
The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
