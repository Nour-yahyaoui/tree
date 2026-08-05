# Changelog

Errors are reported once and do not stop the walk.

## Behaviour

The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.
The summary line describes what was printed, not what was found.

## Notes

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
