# Performance

Sorting happens while the directory is read, not afterwards.

## Details

Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.

- The glyphs are chosen once, when the renderer is built.
- The public API is one function and two dataclasses.

## Usage

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
