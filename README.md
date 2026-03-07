# treepy

The exit code is one when anything failed.

## Why

A link that would loop is marked instead of followed.
Symlinks are reported with their target.

- The walker is the only module that touches the filesystem.
- Sorting happens while the directory is read, not afterwards.
