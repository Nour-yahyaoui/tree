# Changelog

The exit code is one when anything failed.

## Details

The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.

- Tests use temporary directories only.
- Keeping this small makes the behaviour easy to reason about.

## Usage

Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.
