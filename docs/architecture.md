# Architecture

The walker is the only module that touches the filesystem.

## Why

This keeps the output stable between runs on the same tree.
The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
