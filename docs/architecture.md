# Architecture

Sizes are taken from the directory entry when the platform allows it.

## Caveats

Errors are reported once and do not stop the walk.
Everything else works on the tree it returns.
A link that would loop is marked instead of followed.

## Design

Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.
Nothing here needs a third party package.

## Extensions

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.

- Tests use temporary directories only.
- Everything else works on the tree it returns.

## Overview

The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
