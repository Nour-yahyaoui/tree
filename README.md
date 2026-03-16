# treepy

Tests use temporary directories only.

## Behaviour

The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.
The counters are collected during the walk and reused for the summary.

## Notes

A link that would loop is marked instead of followed.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.
