# treepy

The public API is one function and two dataclasses.

## Extensions

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.

## Overview

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.

## Details

The walker is the only module that touches the filesystem.
Symlinks are reported with their target.

- The glyphs are chosen once, when the renderer is built.
- Keeping this small makes the behaviour easy to reason about.

## Usage

The exit code is one when anything failed.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
