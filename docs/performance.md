# Performance

Sizes are taken from the directory entry when the platform allows it.

## Caveats

Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Nothing here needs a third party package.

## Design

Sorting happens while the directory is read, not afterwards.
A directory that cannot be read still appears in the output.

- Patterns are matched against the path relative to the root of the scan.
- Keeping this small makes the behaviour easy to reason about.
