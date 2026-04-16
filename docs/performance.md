# Performance

A directory that cannot be read still appears in the output.

## Design

A link that would loop is marked instead of followed.
The glyphs are chosen once, when the renderer is built.

- Keeping this small makes the behaviour easy to reason about.
- Colour is decided in a single place so the rest stays testable.
