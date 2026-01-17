# Architecture

The public API is one function and two dataclasses.

## Behaviour

Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.

- Nothing here needs a third party package.
- The summary line describes what was printed, not what was found.

## Notes

Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.
The counters are collected during the walk and reused for the summary.
