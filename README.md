# treepy

The glyphs are chosen once, when the renderer is built.

## Extensions

Nothing here needs a third party package.
Symlinks are reported with their target.

- The walker is the only module that touches the filesystem.
- Errors are reported once and do not stop the walk.

## Overview

Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.

## Details

The exit code is one when anything failed.
Errors are reported once and do not stop the walk.
Everything else works on the tree it returns.
Nothing here needs a third party package.

## Usage

Sorting happens while the directory is read, not afterwards.
The glyphs are chosen once, when the renderer is built.

- A directory that cannot be read still appears in the output.
- A link that would loop is marked instead of followed.
