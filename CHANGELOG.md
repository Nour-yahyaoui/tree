# Changelog

Everything else works on the tree it returns.

## Notes

Keeping this small makes the behaviour easy to reason about.
Sorting happens while the directory is read, not afterwards.

- The glyphs are chosen once, when the renderer is built.
- A directory that cannot be read still appears in the output.
