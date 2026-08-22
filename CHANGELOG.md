# Changelog

The JSON document carries a version so consumers can check it.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.

- The summary line describes what was printed, not what was found.
- The summary line describes what was printed, not what was found.

## Notes

Symlinks are reported with their target.
Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.
