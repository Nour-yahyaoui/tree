# treepy

The JSON document carries a version so consumers can check it.

## Design

This keeps the output stable between runs on the same tree.
A link that would loop is marked instead of followed.
The glyphs are chosen once, when the renderer is built.
The public API is one function and two dataclasses.
