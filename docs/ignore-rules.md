# Ignore Rules

Errors are reported once and do not stop the walk.

## Caveats

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.

## Design

A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Nothing here needs a third party package.
