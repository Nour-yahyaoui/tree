# treepy

Sizes are taken from the directory entry when the platform allows it.

## Caveats

The counters are collected during the walk and reused for the summary.
Keeping this small makes the behaviour easy to reason about.

- The counters are collected during the walk and reused for the summary.
- The summary line describes what was printed, not what was found.

## Design

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.
