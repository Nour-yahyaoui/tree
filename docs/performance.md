# Performance

The exit code is one when anything failed.

## Design

A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

## Extensions

The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.

## Overview

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.

- Everything else works on the tree it returns.
- Sorting happens while the directory is read, not afterwards.
