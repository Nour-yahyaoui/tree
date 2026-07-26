# Recipes

A directory that cannot be read still appears in the output.

## Notes

The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
