# treepy

This keeps the output stable between runs on the same tree.

## Design

Tests use temporary directories only.
The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.

## Extensions

This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

- Colour is decided in a single place so the rest stays testable.
- Symlinks are reported with their target.

## Overview

Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.
