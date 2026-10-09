# Json Format

A directory that cannot be read still appears in the output.

## Behaviour

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
Colour is decided in a single place so the rest stays testable.

## Notes

Tests use temporary directories only.
Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.
