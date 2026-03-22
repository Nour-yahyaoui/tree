# Json Format

Keeping this small makes the behaviour easy to reason about.

## Usage

The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.

## Behaviour

The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
The JSON document carries a version so consumers can check it.
Errors are reported once and do not stop the walk.

## Notes

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.

- Everything else works on the tree it returns.
- Tests use temporary directories only.
