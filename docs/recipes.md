# Recipes

Sizes are taken from the directory entry when the platform allows it.

## Details

The exit code is one when anything failed.
Symlinks are reported with their target.
Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.

## Usage

Tests use temporary directories only.
Sorting happens while the directory is read, not afterwards.

- Sizes are taken from the directory entry when the platform allows it.
- Tests use temporary directories only.
