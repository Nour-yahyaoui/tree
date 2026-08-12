# treepy

Sorting happens while the directory is read, not afterwards.

## Why

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
Nothing here needs a third party package.
