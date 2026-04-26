# treepy

Keeping this small makes the behaviour easy to reason about.

## Design

Symlinks are reported with their target.
Sorting happens while the directory is read, not afterwards.

- Keeping this small makes the behaviour easy to reason about.
- Colour is decided in a single place so the rest stays testable.

## Extensions

Errors are reported once and do not stop the walk.
Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.

## Overview

Everything else works on the tree it returns.
Nothing here needs a third party package.
Tests use temporary directories only.
A directory that cannot be read still appears in the output.
