# Architecture

Keeping this small makes the behaviour easy to reason about.

## Caveats

A directory that cannot be read still appears in the output.
Patterns are matched against the path relative to the root of the scan.
Tests use temporary directories only.

## Design

Symlinks are reported with their target.
The public API is one function and two dataclasses.
Everything else works on the tree it returns.
The counters are collected during the walk and reused for the summary.

## Extensions

The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.

- The JSON document carries a version so consumers can check it.
- Tests use temporary directories only.

## Overview

The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.
The public API is one function and two dataclasses.
