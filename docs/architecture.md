# Architecture

Patterns are matched against the path relative to the root of the scan.

## Examples

This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.

## Why

Nothing here needs a third party package.
The JSON document carries a version so consumers can check it.

- This keeps the output stable between runs on the same tree.
- Sizes are taken from the directory entry when the platform allows it.
