# Architecture

A directory that cannot be read still appears in the output.

## Caveats

Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.
Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.

## Design

Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.

- Patterns are matched against the path relative to the root of the scan.
- Nothing here needs a third party package.
