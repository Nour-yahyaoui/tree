# Performance

The walker is the only module that touches the filesystem.

## Behaviour

The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

## Notes

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.

- Sorting happens while the directory is read, not afterwards.
- The counters are collected during the walk and reused for the summary.
