# treepy

Sizes are taken from the directory entry when the platform allows it.

## Examples

Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.

- A directory that cannot be read still appears in the output.
- The glyphs are chosen once, when the renderer is built.

## Why

Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.
The public API is one function and two dataclasses.
