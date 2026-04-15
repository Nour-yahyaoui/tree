# Ignore Rules

The JSON document carries a version so consumers can check it.

## Notes

The public API is one function and two dataclasses.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
