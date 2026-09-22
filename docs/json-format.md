# Json Format

Symlinks are reported with their target.

## Caveats

Nothing here needs a third party package.
The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.

## Design

Symlinks are reported with their target.
Errors are reported once and do not stop the walk.

- The exit code is one when anything failed.
- The public API is one function and two dataclasses.

## Extensions

The glyphs are chosen once, when the renderer is built.
The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

## Overview

The public API is one function and two dataclasses.
Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
