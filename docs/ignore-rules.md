# Ignore Rules

Patterns are matched against the path relative to the root of the scan.

## Usage

The public API is one function and two dataclasses.
Errors are reported once and do not stop the walk.
Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.

## Behaviour

The summary line describes what was printed, not what was found.
Symlinks are reported with their target.

- Sizes are taken from the directory entry when the platform allows it.
- The glyphs are chosen once, when the renderer is built.

## Notes

Sorting happens while the directory is read, not afterwards.
The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.
