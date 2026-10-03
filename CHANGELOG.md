# Changelog

Tests use temporary directories only.

## Details

The exit code is one when anything failed.
Nothing here needs a third party package.

- Sorting happens while the directory is read, not afterwards.
- Sizes are taken from the directory entry when the platform allows it.

## Usage

Nothing here needs a third party package.
The public API is one function and two dataclasses.
Symlinks are reported with their target.
