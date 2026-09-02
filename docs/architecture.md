# Architecture

A link that would loop is marked instead of followed.

## Examples

The counters are collected during the walk and reused for the summary.
Sorting happens while the directory is read, not afterwards.

- Nothing here needs a third party package.
- A directory that cannot be read still appears in the output.

## Why

Patterns are matched against the path relative to the root of the scan.
The public API is one function and two dataclasses.
A link that would loop is marked instead of followed.

## Caveats

Symlinks are reported with their target.
Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.
Patterns are matched against the path relative to the root of the scan.

## Design

Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.

- Patterns are matched against the path relative to the root of the scan.
- Patterns are matched against the path relative to the root of the scan.
