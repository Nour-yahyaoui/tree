# Json Format

The walker is the only module that touches the filesystem.

## Examples

Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.

- The summary line describes what was printed, not what was found.
- Errors are reported once and do not stop the walk.

## Why

This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.
