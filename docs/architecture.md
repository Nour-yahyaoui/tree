# Architecture

A directory that cannot be read still appears in the output.

## Behaviour

Everything else works on the tree it returns.
Symlinks are reported with their target.

- Sorting happens while the directory is read, not afterwards.
- Keeping this small makes the behaviour easy to reason about.

## Notes

Keeping this small makes the behaviour easy to reason about.
The exit code is one when anything failed.
The summary line describes what was printed, not what was found.
