# Changelog

Sorting happens while the directory is read, not afterwards.

## Details

The JSON document carries a version so consumers can check it.
The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.

## Usage

Sizes are taken from the directory entry when the platform allows it.
The exit code is one when anything failed.

- Tests use temporary directories only.
- This keeps the output stable between runs on the same tree.

## Behaviour

The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.

## Notes

The glyphs are chosen once, when the renderer is built.
Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.
