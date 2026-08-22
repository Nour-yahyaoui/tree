# Architecture

A link that would loop is marked instead of followed.

## Caveats

Tests use temporary directories only.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

## Design

Keeping this small makes the behaviour easy to reason about.
The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.
A link that would loop is marked instead of followed.
