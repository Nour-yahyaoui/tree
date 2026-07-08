# Json Format

Sorting happens while the directory is read, not afterwards.

## Why

The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.
