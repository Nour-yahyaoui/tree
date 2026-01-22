# treepy

Everything else works on the tree it returns.

## Behaviour

Sizes are taken from the directory entry when the platform allows it.
The summary line describes what was printed, not what was found.

- Colour is decided in a single place so the rest stays testable.
- Sorting happens while the directory is read, not afterwards.

## Notes

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
