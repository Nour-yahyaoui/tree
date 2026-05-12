# Json Format

Sorting happens while the directory is read, not afterwards.

## Notes

Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.

## Examples

Everything else works on the tree it returns.
Sorting happens while the directory is read, not afterwards.

- The counters are collected during the walk and reused for the summary.
- Symlinks are reported with their target.

## Why

Tests use temporary directories only.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.
