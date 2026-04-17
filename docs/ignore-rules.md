# Ignore Rules

Patterns are matched against the path relative to the root of the scan.

## Behaviour

Symlinks are reported with their target.
The exit code is one when anything failed.
The public API is one function and two dataclasses.
Tests use temporary directories only.

## Notes

The exit code is one when anything failed.
Symlinks are reported with their target.

- Symlinks are reported with their target.
- A directory that cannot be read still appears in the output.
