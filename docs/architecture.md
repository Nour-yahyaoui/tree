# Architecture

Everything else works on the tree it returns.

## Details

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.

- Colour is decided in a single place so the rest stays testable.
- Patterns are matched against the path relative to the root of the scan.

## Usage

Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.

## Behaviour

The exit code is one when anything failed.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.

## Notes

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.

- This keeps the output stable between runs on the same tree.
- The summary line describes what was printed, not what was found.
