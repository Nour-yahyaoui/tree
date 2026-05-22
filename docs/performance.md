# Performance

Colour is decided in a single place so the rest stays testable.

## Overview

Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.
Tests use temporary directories only.
The glyphs are chosen once, when the renderer is built.

## Details

The exit code is one when anything failed.
The walker is the only module that touches the filesystem.

- Patterns are matched against the path relative to the root of the scan.
- Symlinks are reported with their target.

## Usage

This keeps the output stable between runs on the same tree.
Everything else works on the tree it returns.
Tests use temporary directories only.
