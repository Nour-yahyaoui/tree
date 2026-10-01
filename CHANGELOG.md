# Changelog

Nothing here needs a third party package.

## Usage

Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
The exit code is one when anything failed.
The summary line describes what was printed, not what was found.

## Behaviour

The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.

- The walker is the only module that touches the filesystem.
- This keeps the output stable between runs on the same tree.

## Notes

The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.
