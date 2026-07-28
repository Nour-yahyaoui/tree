# treepy

Sizes are taken from the directory entry when the platform allows it.

## Notes

A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.
