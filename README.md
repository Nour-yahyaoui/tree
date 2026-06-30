# treepy

The exit code is one when anything failed.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.
Sizes are taken from the directory entry when the platform allows it.

## Notes

Nothing here needs a third party package.
The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.
Tests use temporary directories only.
