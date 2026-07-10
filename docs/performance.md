# Performance

The glyphs are chosen once, when the renderer is built.

## Extensions

Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

- The public API is one function and two dataclasses.
- The JSON document carries a version so consumers can check it.

## Overview

Sorting happens while the directory is read, not afterwards.
The exit code is one when anything failed.
Errors are reported once and do not stop the walk.

## Details

The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
The exit code is one when anything failed.

## Usage

A directory that cannot be read still appears in the output.
The summary line describes what was printed, not what was found.

- Symlinks are reported with their target.
- Nothing here needs a third party package.
