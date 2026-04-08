# Json Format

Nothing here needs a third party package.

## Caveats

A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
The exit code is one when anything failed.

## Design

Nothing here needs a third party package.
The glyphs are chosen once, when the renderer is built.
The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.
