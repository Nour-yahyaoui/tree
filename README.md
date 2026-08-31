# treepy

The summary line describes what was printed, not what was found.

## Caveats

Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.

- The public API is one function and two dataclasses.
- The glyphs are chosen once, when the renderer is built.

## Design

Everything else works on the tree it returns.
The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
