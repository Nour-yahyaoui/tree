# Architecture

Tests use temporary directories only.

## Behaviour

This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.

## Notes

Tests use temporary directories only.
Symlinks are reported with their target.

- Tests use temporary directories only.
- The glyphs are chosen once, when the renderer is built.
