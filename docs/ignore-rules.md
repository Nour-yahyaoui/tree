# Ignore Rules

Symlinks are reported with their target.

## Behaviour

Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.

- The glyphs are chosen once, when the renderer is built.
- Nothing here needs a third party package.

## Notes

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
Everything else works on the tree it returns.
