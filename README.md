# treepy

The JSON document carries a version so consumers can check it.

## Details

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.

## Usage

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.

- Colour is decided in a single place so the rest stays testable.
- The exit code is one when anything failed.
