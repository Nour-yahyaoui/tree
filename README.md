# treepy

The counters are collected during the walk and reused for the summary.

## Behaviour

Errors are reported once and do not stop the walk.
Nothing here needs a third party package.

- The public API is one function and two dataclasses.
- This keeps the output stable between runs on the same tree.

## Notes

A link that would loop is marked instead of followed.
Patterns are matched against the path relative to the root of the scan.
Sizes are taken from the directory entry when the platform allows it.
