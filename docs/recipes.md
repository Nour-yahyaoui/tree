# Recipes

Nothing here needs a third party package.

## Notes

Keeping this small makes the behaviour easy to reason about.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
Nothing here needs a third party package.

## Examples

A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.

- Patterns are matched against the path relative to the root of the scan.
- The exit code is one when anything failed.

## Why

The summary line describes what was printed, not what was found.
The public API is one function and two dataclasses.
Nothing here needs a third party package.
