# treepy

The summary line describes what was printed, not what was found.

## Behaviour

The walker is the only module that touches the filesystem.
Nothing here needs a third party package.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.

## Notes

The glyphs are chosen once, when the renderer is built.
Patterns are matched against the path relative to the root of the scan.

- The counters are collected during the walk and reused for the summary.
- The public API is one function and two dataclasses.
