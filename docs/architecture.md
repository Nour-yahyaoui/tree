# Architecture

Patterns are matched against the path relative to the root of the scan.

## Notes

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
