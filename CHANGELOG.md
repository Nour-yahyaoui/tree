# Changelog

Sorting happens while the directory is read, not afterwards.

## Overview

Tests use temporary directories only.
The counters are collected during the walk and reused for the summary.

- The walker is the only module that touches the filesystem.
- Sizes are taken from the directory entry when the platform allows it.

## Details

Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.
Sorting happens while the directory is read, not afterwards.

## Usage

The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.
Nothing here needs a third party package.
The public API is one function and two dataclasses.
