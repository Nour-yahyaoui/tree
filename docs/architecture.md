# Architecture

The glyphs are chosen once, when the renderer is built.

## Design

Sorting happens while the directory is read, not afterwards.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.

## Extensions

The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.

- Colour is decided in a single place so the rest stays testable.
- The glyphs are chosen once, when the renderer is built.

## Overview

The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
