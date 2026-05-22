# Ignore Rules

The glyphs are chosen once, when the renderer is built.

## Usage

Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.
