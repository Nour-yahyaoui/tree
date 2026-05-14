# Ignore Rules

Errors are reported once and do not stop the walk.

## Overview

A directory that cannot be read still appears in the output.
The exit code is one when anything failed.

- Symlinks are reported with their target.
- The public API is one function and two dataclasses.

## Details

Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.

## Usage

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
