# Performance

A link that would loop is marked instead of followed.

## Caveats

Symlinks are reported with their target.
Sorting happens while the directory is read, not afterwards.

- Sizes are taken from the directory entry when the platform allows it.
- Sorting happens while the directory is read, not afterwards.

## Design

Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.
A directory that cannot be read still appears in the output.
