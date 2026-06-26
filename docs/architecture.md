# Architecture

The glyphs are chosen once, when the renderer is built.

## Usage

Tests use temporary directories only.
Everything else works on the tree it returns.
The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.
