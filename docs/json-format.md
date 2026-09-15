# Json Format

Nothing here needs a third party package.

## Details

Symlinks are reported with their target.
The walker is the only module that touches the filesystem.

- Symlinks are reported with their target.
- The glyphs are chosen once, when the renderer is built.

## Usage

The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.
