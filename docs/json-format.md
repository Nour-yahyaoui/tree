# Json Format

The exit code is one when anything failed.

## Examples

A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.
Tests use temporary directories only.

## Why

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.

- A directory that cannot be read still appears in the output.
- Colour is decided in a single place so the rest stays testable.
