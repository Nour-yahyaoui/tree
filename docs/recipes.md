# Recipes

Colour is decided in a single place so the rest stays testable.

## Details

Tests use temporary directories only.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

## Usage

The glyphs are chosen once, when the renderer is built.
The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

## Behaviour

The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.

- Nothing here needs a third party package.
- The glyphs are chosen once, when the renderer is built.

## Notes

The glyphs are chosen once, when the renderer is built.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
