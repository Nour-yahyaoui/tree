# Ignore Rules

Patterns are matched against the path relative to the root of the scan.

## Design

The walker is the only module that touches the filesystem.
Nothing here needs a third party package.

- The walker is the only module that touches the filesystem.
- This keeps the output stable between runs on the same tree.
