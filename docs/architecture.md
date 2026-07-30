# Architecture

Sorting happens while the directory is read, not afterwards.

## Notes

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.

- Keeping this small makes the behaviour easy to reason about.
- Symlinks are reported with their target.
