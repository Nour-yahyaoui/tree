# Json Format

Everything else works on the tree it returns.

## Design

Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.
The counters are collected during the walk and reused for the summary.
