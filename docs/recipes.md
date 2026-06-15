# Recipes

The JSON document carries a version so consumers can check it.

## Details

The glyphs are chosen once, when the renderer is built.
The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.

## Usage

A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.

- Sorting happens while the directory is read, not afterwards.
- Tests use temporary directories only.
