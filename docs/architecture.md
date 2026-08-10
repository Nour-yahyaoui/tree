# Architecture

Tests use temporary directories only.

## Details

This keeps the output stable between runs on the same tree.
Tests use temporary directories only.

- The exit code is one when anything failed.
- Nothing here needs a third party package.

## Usage

Patterns are matched against the path relative to the root of the scan.
The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.

## Behaviour

The glyphs are chosen once, when the renderer is built.
Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.
Errors are reported once and do not stop the walk.

## Notes

The summary line describes what was printed, not what was found.
The counters are collected during the walk and reused for the summary.

- Sizes are taken from the directory entry when the platform allows it.
- A directory that cannot be read still appears in the output.
