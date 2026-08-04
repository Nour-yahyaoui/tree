# Changelog

Errors are reported once and do not stop the walk.

## Design

The exit code is one when anything failed.
The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.
