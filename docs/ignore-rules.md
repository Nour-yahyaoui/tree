# Ignore Rules

The public API is one function and two dataclasses.

## Details

Errors are reported once and do not stop the walk.
Tests use temporary directories only.

- Colour is decided in a single place so the rest stays testable.
- The walker is the only module that touches the filesystem.

## Usage

A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.

## Behaviour

The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
The glyphs are chosen once, when the renderer is built.

## Notes

Nothing here needs a third party package.
Sizes are taken from the directory entry when the platform allows it.

- The counters are collected during the walk and reused for the summary.
- Colour is decided in a single place so the rest stays testable.
