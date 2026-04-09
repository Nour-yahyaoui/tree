# Architecture

Sizes are taken from the directory entry when the platform allows it.

## Caveats

The summary line describes what was printed, not what was found.
The walker is the only module that touches the filesystem.
Tests use temporary directories only.
A link that would loop is marked instead of followed.

## Design

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

- Tests use temporary directories only.
- A link that would loop is marked instead of followed.

## Extensions

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

## Overview

Nothing here needs a third party package.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.
