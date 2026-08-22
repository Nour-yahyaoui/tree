# treepy

The public API is one function and two dataclasses.

## Details

The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.

## Usage

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
Symlinks are reported with their target.

## Behaviour

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.

- Sizes are taken from the directory entry when the platform allows it.
- Nothing here needs a third party package.

## Notes

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.
