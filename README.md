# treepy

Colour is decided in a single place so the rest stays testable.

## Caveats

The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.
Tests use temporary directories only.

## Design

Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.

- The counters are collected during the walk and reused for the summary.
- Sorting happens while the directory is read, not afterwards.
