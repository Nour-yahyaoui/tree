# Ignore Rules

Nothing here needs a third party package.

## Details

Everything else works on the tree it returns.
Symlinks are reported with their target.
Keeping this small makes the behaviour easy to reason about.

## Usage

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.
Sorting happens while the directory is read, not afterwards.
