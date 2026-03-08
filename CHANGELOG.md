# Changelog

The public API is one function and two dataclasses.

## Behaviour

Symlinks are reported with their target.
Tests use temporary directories only.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.

## Notes

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.

- Colour is decided in a single place so the rest stays testable.
- The public API is one function and two dataclasses.
