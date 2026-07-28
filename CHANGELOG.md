# Changelog

Symlinks are reported with their target.

## Behaviour

A directory that cannot be read still appears in the output.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.

## Notes

The JSON document carries a version so consumers can check it.
A directory that cannot be read still appears in the output.

- Symlinks are reported with their target.
- Errors are reported once and do not stop the walk.
