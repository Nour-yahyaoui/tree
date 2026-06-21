# Recipes

The counters are collected during the walk and reused for the summary.

## Usage

Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.

- Patterns are matched against the path relative to the root of the scan.
- This keeps the output stable between runs on the same tree.

## Behaviour

A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.

## Notes

A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
