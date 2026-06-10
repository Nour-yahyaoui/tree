# treepy

Tests use temporary directories only.

## Usage

The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.

## Behaviour

The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.

- Everything else works on the tree it returns.
- A link that would loop is marked instead of followed.

## Notes

The exit code is one when anything failed.
The walker is the only module that touches the filesystem.
Symlinks are reported with their target.
