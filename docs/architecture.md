# Architecture

The exit code is one when anything failed.

## Why

The glyphs are chosen once, when the renderer is built.
Tests use temporary directories only.
A link that would loop is marked instead of followed.
Nothing here needs a third party package.
