# Changelog

The JSON document carries a version so consumers can check it.

## Overview

Tests use temporary directories only.
The counters are collected during the walk and reused for the summary.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.

## Details

The glyphs are chosen once, when the renderer is built.
The walker is the only module that touches the filesystem.

- A directory that cannot be read still appears in the output.
- The walker is the only module that touches the filesystem.

## Usage

The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.
