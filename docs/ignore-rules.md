# Ignore Rules

Sizes are taken from the directory entry when the platform allows it.

## Behaviour

Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.
Nothing here needs a third party package.
Keeping this small makes the behaviour easy to reason about.

## Notes

Sizes are taken from the directory entry when the platform allows it.
A directory that cannot be read still appears in the output.

- Patterns are matched against the path relative to the root of the scan.
- Everything else works on the tree it returns.
