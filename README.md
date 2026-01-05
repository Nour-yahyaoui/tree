# treepy

Colour is decided in a single place so the rest stays testable.

## Design

The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.

- The glyphs are chosen once, when the renderer is built.
- A link that would loop is marked instead of followed.
