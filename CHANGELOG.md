# Changelog

Sizes are taken from the directory entry when the platform allows it.

## Behaviour

A directory that cannot be read still appears in the output.
Patterns are matched against the path relative to the root of the scan.

- Patterns are matched against the path relative to the root of the scan.
- Keeping this small makes the behaviour easy to reason about.

## Notes

A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.
