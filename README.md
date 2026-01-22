# treepy

Symlinks are reported with their target.

## Caveats

Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.

## Design

A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.
The counters are collected during the walk and reused for the summary.
