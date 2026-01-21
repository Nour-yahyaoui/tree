# Performance

The counters are collected during the walk and reused for the summary.

## Caveats

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.

- Patterns are matched against the path relative to the root of the scan.
- The walker is the only module that touches the filesystem.

## Design

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.

## Extensions

Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.
The glyphs are chosen once, when the renderer is built.

## Overview

Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.

- Everything else works on the tree it returns.
- Colour is decided in a single place so the rest stays testable.
