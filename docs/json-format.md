# Json Format

Errors are reported once and do not stop the walk.

## Notes

Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.
