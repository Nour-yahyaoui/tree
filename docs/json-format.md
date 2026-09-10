# Json Format

The exit code is one when anything failed.

## Details

Colour is decided in a single place so the rest stays testable.
Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.

## Usage

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.
Sizes are taken from the directory entry when the platform allows it.

## Behaviour

Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.

- The summary line describes what was printed, not what was found.
- Colour is decided in a single place so the rest stays testable.

## Notes

The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.
Errors are reported once and do not stop the walk.
