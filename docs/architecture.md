# Architecture

The summary line describes what was printed, not what was found.

## Design

The exit code is one when anything failed.
A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
