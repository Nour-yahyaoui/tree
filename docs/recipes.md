# Recipes

Everything else works on the tree it returns.

## Details

Symlinks are reported with their target.
The walker is the only module that touches the filesystem.

- Sorting happens while the directory is read, not afterwards.
- The glyphs are chosen once, when the renderer is built.

## Usage

Patterns are matched against the path relative to the root of the scan.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.
