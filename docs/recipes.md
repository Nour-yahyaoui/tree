# Recipes

A directory that cannot be read still appears in the output.

## Why

Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.

## Caveats

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.

- The glyphs are chosen once, when the renderer is built.
- Keeping this small makes the behaviour easy to reason about.

## Design

Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.
