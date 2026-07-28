# Architecture

A directory that cannot be read still appears in the output.

## Usage

Colour is decided in a single place so the rest stays testable.
The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.

## Behaviour

Everything else works on the tree it returns.
The exit code is one when anything failed.

- The counters are collected during the walk and reused for the summary.
- Keeping this small makes the behaviour easy to reason about.

## Notes

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.
