# Json Format

Errors are reported once and do not stop the walk.

## Notes

Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.

- Symlinks are reported with their target.
- Sorting happens while the directory is read, not afterwards.
