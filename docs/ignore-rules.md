# Ignore Rules

Tests use temporary directories only.

## Caveats

Tests use temporary directories only.
Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.

## Design

The glyphs are chosen once, when the renderer is built.
Errors are reported once and do not stop the walk.
Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.

## Extensions

Errors are reported once and do not stop the walk.
The counters are collected during the walk and reused for the summary.

- The JSON document carries a version so consumers can check it.
- Patterns are matched against the path relative to the root of the scan.

## Overview

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.
