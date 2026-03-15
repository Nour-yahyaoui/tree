# Recipes

The summary line describes what was printed, not what was found.

## Usage

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.

## Behaviour

A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.

- The summary line describes what was printed, not what was found.
- Everything else works on the tree it returns.

## Notes

Tests use temporary directories only.
The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.
