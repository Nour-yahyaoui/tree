# Architecture

Everything else works on the tree it returns.

## Details

Tests use temporary directories only.
The JSON document carries a version so consumers can check it.

- The walker is the only module that touches the filesystem.
- The public API is one function and two dataclasses.

## Usage

The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
