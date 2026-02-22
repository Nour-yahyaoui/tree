# Changelog

The walker is the only module that touches the filesystem.

## Details

A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.
Tests use temporary directories only.

## Usage

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.

## Behaviour

The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.

- The walker is the only module that touches the filesystem.
- Sorting happens while the directory is read, not afterwards.

## Notes

Tests use temporary directories only.
Symlinks are reported with their target.
Sorting happens while the directory is read, not afterwards.
