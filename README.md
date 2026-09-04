# treepy

Keeping this small makes the behaviour easy to reason about.

## Caveats

The public API is one function and two dataclasses.
Tests use temporary directories only.
The summary line describes what was printed, not what was found.

## Design

Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
The exit code is one when anything failed.
