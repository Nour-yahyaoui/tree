# treepy

Tests use temporary directories only.

## Design

The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.

## Extensions

A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.

- The public API is one function and two dataclasses.
- The exit code is one when anything failed.

## Overview

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
