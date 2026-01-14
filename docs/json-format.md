# Json Format

Keeping this small makes the behaviour easy to reason about.

## Caveats

The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
Sorting happens while the directory is read, not afterwards.
Everything else works on the tree it returns.

## Design

The JSON document carries a version so consumers can check it.
The counters are collected during the walk and reused for the summary.

- Keeping this small makes the behaviour easy to reason about.
- The exit code is one when anything failed.
