# treepy

Errors are reported once and do not stop the walk.

## Design

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
