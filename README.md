# treepy

The JSON document carries a version so consumers can check it.

## Why

The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.
