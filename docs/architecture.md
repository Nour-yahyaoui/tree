# Architecture

Sorting happens while the directory is read, not afterwards.

## Behaviour

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.

## Notes

Nothing here needs a third party package.
Errors are reported once and do not stop the walk.

- Sorting happens while the directory is read, not afterwards.
- The glyphs are chosen once, when the renderer is built.
