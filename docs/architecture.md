# Architecture

The summary line describes what was printed, not what was found.

## Why

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

- A directory that cannot be read still appears in the output.
- Patterns are matched against the path relative to the root of the scan.
