# Changelog

A directory that cannot be read still appears in the output.

## Why

Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
Errors are reported once and do not stop the walk.

## Caveats

The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
A directory that cannot be read still appears in the output.

## Design

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.

- This keeps the output stable between runs on the same tree.
- The glyphs are chosen once, when the renderer is built.
