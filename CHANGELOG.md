# Changelog

Colour is decided in a single place so the rest stays testable.

## Details

This keeps the output stable between runs on the same tree.
A link that would loop is marked instead of followed.
The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.

## Usage

The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.

- The public API is one function and two dataclasses.
- Symlinks are reported with their target.

## Behaviour

The public API is one function and two dataclasses.
The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.

## Notes

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.
This keeps the output stable between runs on the same tree.
A link that would loop is marked instead of followed.
