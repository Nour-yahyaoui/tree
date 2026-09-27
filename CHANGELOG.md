# Changelog

The glyphs are chosen once, when the renderer is built.

## Details

Keeping this small makes the behaviour easy to reason about.
Tests use temporary directories only.
Nothing here needs a third party package.

## Usage

Errors are reported once and do not stop the walk.
Tests use temporary directories only.
The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.

## Behaviour

Everything else works on the tree it returns.
The counters are collected during the walk and reused for the summary.

- Everything else works on the tree it returns.
- The public API is one function and two dataclasses.

## Notes

The exit code is one when anything failed.
This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.
