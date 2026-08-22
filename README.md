# treepy

The summary line describes what was printed, not what was found.

## Caveats

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

- Sorting happens while the directory is read, not afterwards.
- The public API is one function and two dataclasses.

## Design

Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

## Extensions

Nothing here needs a third party package.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

## Overview

This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.

- The glyphs are chosen once, when the renderer is built.
- Keeping this small makes the behaviour easy to reason about.
