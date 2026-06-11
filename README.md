# treepy

Errors are reported once and do not stop the walk.

## Why

Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.

- The counters are collected during the walk and reused for the summary.
- Keeping this small makes the behaviour easy to reason about.

## Caveats

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.
Nothing here needs a third party package.

## Design

The glyphs are chosen once, when the renderer is built.
Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.
