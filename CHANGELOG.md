# Changelog

The summary line describes what was printed, not what was found.

## Why

This keeps the output stable between runs on the same tree.
The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
