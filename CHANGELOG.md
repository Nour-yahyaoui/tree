# Changelog

Sorting happens while the directory is read, not afterwards.

## Caveats

Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.

- The public API is one function and two dataclasses.
- The summary line describes what was printed, not what was found.

## Design

Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.
Everything else works on the tree it returns.
