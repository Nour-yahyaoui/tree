# Architecture

Everything else works on the tree it returns.

## Caveats

The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.

- Everything else works on the tree it returns.
- A directory that cannot be read still appears in the output.

## Design

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
