# treepy

The exit code is one when anything failed.

## Caveats

Keeping this small makes the behaviour easy to reason about.
This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.
The public API is one function and two dataclasses.

## Design

The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.

- Sizes are taken from the directory entry when the platform allows it.
- The counters are collected during the walk and reused for the summary.
