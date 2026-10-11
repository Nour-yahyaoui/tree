# Ignore Rules

Nothing here needs a third party package.

## Details

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
The counters are collected during the walk and reused for the summary.

## Usage

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
Sizes are taken from the directory entry when the platform allows it.

## Behaviour

Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.

- This keeps the output stable between runs on the same tree.
- A directory that cannot be read still appears in the output.

## Notes

A directory that cannot be read still appears in the output.
The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.
