# Json Format

Nothing here needs a third party package.

## Caveats

Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
The exit code is one when anything failed.
A link that would loop is marked instead of followed.

## Design

A directory that cannot be read still appears in the output.
Symlinks are reported with their target.

- Nothing here needs a third party package.
- This keeps the output stable between runs on the same tree.
