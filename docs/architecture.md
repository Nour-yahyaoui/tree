# Architecture

Patterns are matched against the path relative to the root of the scan.

## Caveats

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.

- Sizes are taken from the directory entry when the platform allows it.
- The glyphs are chosen once, when the renderer is built.

## Design

The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.
