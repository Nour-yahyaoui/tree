# Performance

Sorting happens while the directory is read, not afterwards.

## Usage

Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

- A directory that cannot be read still appears in the output.
- Errors are reported once and do not stop the walk.

## Behaviour

This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

## Notes

Tests use temporary directories only.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
A link that would loop is marked instead of followed.
