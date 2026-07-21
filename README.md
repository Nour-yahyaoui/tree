# treepy

Tests use temporary directories only.

## Caveats

The public API is one function and two dataclasses.
The counters are collected during the walk and reused for the summary.

- Sizes are taken from the directory entry when the platform allows it.
- Sizes are taken from the directory entry when the platform allows it.

## Design

A directory that cannot be read still appears in the output.
This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
