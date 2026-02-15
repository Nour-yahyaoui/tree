# treepy

The counters are collected during the walk and reused for the summary.

## Usage

Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.

## Behaviour

A directory that cannot be read still appears in the output.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.

## Notes

A link that would loop is marked instead of followed.
The public API is one function and two dataclasses.

- A directory that cannot be read still appears in the output.
- The summary line describes what was printed, not what was found.
