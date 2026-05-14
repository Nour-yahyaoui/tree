# Architecture

Errors are reported once and do not stop the walk.

## Usage

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.
