# treepy

This keeps the output stable between runs on the same tree.

## Extensions

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Symlinks are reported with their target.

## Overview

The public API is one function and two dataclasses.
Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
Nothing here needs a third party package.

## Details

The walker is the only module that touches the filesystem.
Tests use temporary directories only.

- The walker is the only module that touches the filesystem.
- The counters are collected during the walk and reused for the summary.

## Usage

The counters are collected during the walk and reused for the summary.
Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.
