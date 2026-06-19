# Json Format

The public API is one function and two dataclasses.

## Examples

Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.

- Tests use temporary directories only.
- A link that would loop is marked instead of followed.

## Why

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.
Tests use temporary directories only.

## Caveats

Everything else works on the tree it returns.
The exit code is one when anything failed.
A directory that cannot be read still appears in the output.
Nothing here needs a third party package.

## Design

Sizes are taken from the directory entry when the platform allows it.
Keeping this small makes the behaviour easy to reason about.

- Sorting happens while the directory is read, not afterwards.
- Patterns are matched against the path relative to the root of the scan.
