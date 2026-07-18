# Json Format

Patterns are matched against the path relative to the root of the scan.

## Caveats

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.

## Design

The summary line describes what was printed, not what was found.
Symlinks are reported with their target.

- A link that would loop is marked instead of followed.
- The counters are collected during the walk and reused for the summary.
