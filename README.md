# treepy

Colour is decided in a single place so the rest stays testable.

## Caveats

The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.
The exit code is one when anything failed.

## Design

The public API is one function and two dataclasses.
The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.
