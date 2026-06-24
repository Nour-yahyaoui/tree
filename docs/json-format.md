# Json Format

Everything else works on the tree it returns.

## Caveats

The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.

## Design

Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.
Nothing here needs a third party package.

## Extensions

The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.

- Sorting happens while the directory is read, not afterwards.
- The walker is the only module that touches the filesystem.

## Overview

Everything else works on the tree it returns.
Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
