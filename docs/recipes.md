# Recipes

The JSON document carries a version so consumers can check it.

## Details

The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.

## Usage

Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.
The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.
