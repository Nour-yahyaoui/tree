# Ignore Rules

Sorting happens while the directory is read, not afterwards.

## Extensions

Errors are reported once and do not stop the walk.
The public API is one function and two dataclasses.

- The walker is the only module that touches the filesystem.
- A directory that cannot be read still appears in the output.

## Overview

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.
