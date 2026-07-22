# Recipes

A link that would loop is marked instead of followed.

## Details

The JSON document carries a version so consumers can check it.
Tests use temporary directories only.
The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.

## Usage

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

- Sorting happens while the directory is read, not afterwards.
- The public API is one function and two dataclasses.

## Behaviour

The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.
Colour is decided in a single place so the rest stays testable.

## Notes

Symlinks are reported with their target.
The walker is the only module that touches the filesystem.
This keeps the output stable between runs on the same tree.
Sorting happens while the directory is read, not afterwards.
