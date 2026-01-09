# treepy

The summary line describes what was printed, not what was found.

## Behaviour

Errors are reported once and do not stop the walk.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
The glyphs are chosen once, when the renderer is built.

## Notes

A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.

- The exit code is one when anything failed.
- The public API is one function and two dataclasses.

## Examples

Sizes are taken from the directory entry when the platform allows it.
Tests use temporary directories only.
A directory that cannot be read still appears in the output.

## Why

Colour is decided in a single place so the rest stays testable.
The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
