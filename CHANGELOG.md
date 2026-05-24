# Changelog

Sorting happens while the directory is read, not afterwards.

## Usage

Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.

- Colour is decided in a single place so the rest stays testable.
- The public API is one function and two dataclasses.
