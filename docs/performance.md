# Performance

Sorting happens while the directory is read, not afterwards.

## Details

Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.

## Usage

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.

- Tests use temporary directories only.
- The summary line describes what was printed, not what was found.

## Behaviour

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
Tests use temporary directories only.

## Notes

Keeping this small makes the behaviour easy to reason about.
Nothing here needs a third party package.
The exit code is one when anything failed.
Sorting happens while the directory is read, not afterwards.
