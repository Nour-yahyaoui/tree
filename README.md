# treepy

Colour is decided in a single place so the rest stays testable.

## Behaviour

The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
Errors are reported once and do not stop the walk.

## Notes

This keeps the output stable between runs on the same tree.
A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.
