# Ignore Rules

Symlinks are reported with their target.

## Behaviour

A directory that cannot be read still appears in the output.
The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.

## Notes

Patterns are matched against the path relative to the root of the scan.
Sizes are taken from the directory entry when the platform allows it.
Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.

## Examples

The summary line describes what was printed, not what was found.
The JSON document carries a version so consumers can check it.

- Colour is decided in a single place so the rest stays testable.
- The glyphs are chosen once, when the renderer is built.

## Why

Nothing here needs a third party package.
The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
