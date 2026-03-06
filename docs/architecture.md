# Architecture

Nothing here needs a third party package.

## Caveats

A directory that cannot be read still appears in the output.
Patterns are matched against the path relative to the root of the scan.

- Sizes are taken from the directory entry when the platform allows it.
- Tests use temporary directories only.

## Design

Symlinks are reported with their target.
The exit code is one when anything failed.
A link that would loop is marked instead of followed.

## Extensions

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.
A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.

## Overview

The glyphs are chosen once, when the renderer is built.
The exit code is one when anything failed.

- The counters are collected during the walk and reused for the summary.
- The public API is one function and two dataclasses.
