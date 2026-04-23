# Ignore Rules

This keeps the output stable between runs on the same tree.

## Behaviour

Sizes are taken from the directory entry when the platform allows it.
The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
The public API is one function and two dataclasses.

## Notes

Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

- A directory that cannot be read still appears in the output.
- Errors are reported once and do not stop the walk.
