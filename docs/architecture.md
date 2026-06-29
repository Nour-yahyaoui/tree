# Architecture

The JSON document carries a version so consumers can check it.

## Design

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.

## Extensions

Patterns are matched against the path relative to the root of the scan.
Everything else works on the tree it returns.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.

## Overview

Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.

- The walker is the only module that touches the filesystem.
- This keeps the output stable between runs on the same tree.
