# Architecture

The walker is the only module that touches the filesystem.

## Design

This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.

- Keeping this small makes the behaviour easy to reason about.
- Sizes are taken from the directory entry when the platform allows it.

## Extensions

The exit code is one when anything failed.
The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.

## Overview

Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
The exit code is one when anything failed.
