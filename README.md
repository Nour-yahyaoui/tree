# treepy

The walker is the only module that touches the filesystem.

## Extensions

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.
Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.

## Overview

The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.

- A directory that cannot be read still appears in the output.
- Sizes are taken from the directory entry when the platform allows it.

## Details

The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.

## Usage

Colour is decided in a single place so the rest stays testable.
The exit code is one when anything failed.
Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
