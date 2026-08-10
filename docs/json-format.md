# Json Format

The glyphs are chosen once, when the renderer is built.

## Behaviour

Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.
Nothing here needs a third party package.

## Notes

A directory that cannot be read still appears in the output.
A link that would loop is marked instead of followed.

- The glyphs are chosen once, when the renderer is built.
- Sizes are taken from the directory entry when the platform allows it.
