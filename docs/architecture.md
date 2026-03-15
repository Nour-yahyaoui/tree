# Architecture

Errors are reported once and do not stop the walk.

## Design

The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.
The glyphs are chosen once, when the renderer is built.
