# Json Format

Patterns are matched against the path relative to the root of the scan.

## Design

The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Errors are reported once and do not stop the walk.

## Extensions

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
The summary line describes what was printed, not what was found.

## Overview

A link that would loop is marked instead of followed.
Everything else works on the tree it returns.

- Symlinks are reported with their target.
- The JSON document carries a version so consumers can check it.
