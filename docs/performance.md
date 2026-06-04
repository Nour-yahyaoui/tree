# Performance

The glyphs are chosen once, when the renderer is built.

## Overview

Sorting happens while the directory is read, not afterwards.
Sizes are taken from the directory entry when the platform allows it.
Nothing here needs a third party package.

## Details

Errors are reported once and do not stop the walk.
Everything else works on the tree it returns.
Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.

## Usage

The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.

- Symlinks are reported with their target.
- Sorting happens while the directory is read, not afterwards.
