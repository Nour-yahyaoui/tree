# Performance

Colour is decided in a single place so the rest stays testable.

## Details

Everything else works on the tree it returns.
The exit code is one when anything failed.
A link that would loop is marked instead of followed.
Tests use temporary directories only.

## Usage

Sorting happens while the directory is read, not afterwards.
The counters are collected during the walk and reused for the summary.

- Errors are reported once and do not stop the walk.
- The public API is one function and two dataclasses.
