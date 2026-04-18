# Json Format

The exit code is one when anything failed.

## Design

Patterns are matched against the path relative to the root of the scan.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.
