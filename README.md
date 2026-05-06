# treepy

The summary line describes what was printed, not what was found.

## Design

The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.
