# Recipes

A link that would loop is marked instead of followed.

## Caveats

Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.

- Sizes are taken from the directory entry when the platform allows it.
- A directory that cannot be read still appears in the output.

## Design

A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.

## Extensions

Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.

## Overview

Tests use temporary directories only.
Everything else works on the tree it returns.

- A directory that cannot be read still appears in the output.
- The counters are collected during the walk and reused for the summary.
