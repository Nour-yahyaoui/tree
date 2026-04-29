# Changelog

The public API is one function and two dataclasses.

## Behaviour

Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.

## Notes

A link that would loop is marked instead of followed.
Nothing here needs a third party package.

- The walker is the only module that touches the filesystem.
- Keeping this small makes the behaviour easy to reason about.
