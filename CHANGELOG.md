# Changelog

Nothing here needs a third party package.

## Why

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.
The summary line describes what was printed, not what was found.
The exit code is one when anything failed.

## Caveats

The exit code is one when anything failed.
Tests use temporary directories only.

- A directory that cannot be read still appears in the output.
- Errors are reported once and do not stop the walk.

## Design

Sorting happens while the directory is read, not afterwards.
The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.
