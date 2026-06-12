# Recipes

A directory that cannot be read still appears in the output.

## Notes

A directory that cannot be read still appears in the output.
The JSON document carries a version so consumers can check it.

- The walker is the only module that touches the filesystem.
- Errors are reported once and do not stop the walk.
