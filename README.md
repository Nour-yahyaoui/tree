# treepy

Errors are reported once and do not stop the walk.

## Caveats

Everything else works on the tree it returns.
A link that would loop is marked instead of followed.
Tests use temporary directories only.

## Design

Sizes are taken from the directory entry when the platform allows it.
Symlinks are reported with their target.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Extensions

The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.

- Symlinks are reported with their target.
- A link that would loop is marked instead of followed.

## Overview

A link that would loop is marked instead of followed.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
