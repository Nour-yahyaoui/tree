# Architecture

Errors are reported once and do not stop the walk.

## Details

This keeps the output stable between runs on the same tree.
Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.

## Usage

The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

- The counters are collected during the walk and reused for the summary.
- Sizes are taken from the directory entry when the platform allows it.
