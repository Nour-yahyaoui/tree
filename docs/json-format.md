# Json Format

The public API is one function and two dataclasses.

## Design

A directory that cannot be read still appears in the output.
Tests use temporary directories only.
Errors are reported once and do not stop the walk.
