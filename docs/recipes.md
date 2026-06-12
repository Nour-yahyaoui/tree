# Recipes

Symlinks are reported with their target.

## Design

Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.

- Tests use temporary directories only.
- Everything else works on the tree it returns.

## Extensions

Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.

## Overview

The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
Colour is decided in a single place so the rest stays testable.
