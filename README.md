# treepy

A link that would loop is marked instead of followed.

## Usage

The summary line describes what was printed, not what was found.
Errors are reported once and do not stop the walk.

- The glyphs are chosen once, when the renderer is built.
- Symlinks are reported with their target.

## Behaviour

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.

## Notes

Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
