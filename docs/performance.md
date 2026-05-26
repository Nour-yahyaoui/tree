# Performance

Sorting happens while the directory is read, not afterwards.

## Why

A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.

- Sorting happens while the directory is read, not afterwards.
- The JSON document carries a version so consumers can check it.
