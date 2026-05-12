# Changelog

The glyphs are chosen once, when the renderer is built.

## Extensions

The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.

## Overview

The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.

## Details

Sorting happens while the directory is read, not afterwards.
Sizes are taken from the directory entry when the platform allows it.

- The counters are collected during the walk and reused for the summary.
- Everything else works on the tree it returns.

## Usage

Tests use temporary directories only.
Symlinks are reported with their target.
The JSON document carries a version so consumers can check it.
