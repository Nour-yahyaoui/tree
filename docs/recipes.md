# Recipes

The glyphs are chosen once, when the renderer is built.

## Usage

The JSON document carries a version so consumers can check it.
Tests use temporary directories only.
The exit code is one when anything failed.

## Behaviour

The counters are collected during the walk and reused for the summary.
Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.

## Notes

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.

- Sorting happens while the directory is read, not afterwards.
- Sizes are taken from the directory entry when the platform allows it.
