# Recipes

The public API is one function and two dataclasses.

## Details

Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.

- Colour is decided in a single place so the rest stays testable.
- The summary line describes what was printed, not what was found.

## Usage

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
