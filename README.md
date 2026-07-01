# treepy

A directory that cannot be read still appears in the output.

## Usage

Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.

## Behaviour

This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.
Sizes are taken from the directory entry when the platform allows it.
Symlinks are reported with their target.

## Notes

The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.

- Symlinks are reported with their target.
- A link that would loop is marked instead of followed.
