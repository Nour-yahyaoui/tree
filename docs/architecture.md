# Architecture

Symlinks are reported with their target.

## Why

The public API is one function and two dataclasses.
A link that would loop is marked instead of followed.
Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.

## Caveats

The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.

- This keeps the output stable between runs on the same tree.
- This keeps the output stable between runs on the same tree.

## Design

The summary line describes what was printed, not what was found.
The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.
