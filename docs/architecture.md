# Architecture

Colour is decided in a single place so the rest stays testable.

## Caveats

The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Symlinks are reported with their target.

## Design

A directory that cannot be read still appears in the output.
Nothing here needs a third party package.

- Everything else works on the tree it returns.
- A link that would loop is marked instead of followed.
