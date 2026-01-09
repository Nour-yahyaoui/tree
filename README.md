# treepy

The walker is the only module that touches the filesystem.

## Usage

The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.
The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.
