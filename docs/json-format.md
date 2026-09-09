# Json Format

Tests use temporary directories only.

## Usage

The public API is one function and two dataclasses.
The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.

## Behaviour

The public API is one function and two dataclasses.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.

## Notes

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.

- Tests use temporary directories only.
- This keeps the output stable between runs on the same tree.
