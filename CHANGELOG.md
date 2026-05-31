# Changelog

The counters are collected during the walk and reused for the summary.

## Notes

Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.
Sorting happens while the directory is read, not afterwards.

## Examples

Nothing here needs a third party package.
A directory that cannot be read still appears in the output.
Symlinks are reported with their target.
The counters are collected during the walk and reused for the summary.

## Why

This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.

- Patterns are matched against the path relative to the root of the scan.
- A link that would loop is marked instead of followed.
