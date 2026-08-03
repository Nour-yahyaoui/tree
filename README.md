# treepy

The walker is the only module that touches the filesystem.

## Caveats

Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.

- Symlinks are reported with their target.
- The summary line describes what was printed, not what was found.

## Design

The counters are collected during the walk and reused for the summary.
The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
