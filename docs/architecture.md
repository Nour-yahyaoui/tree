# Architecture

The counters are collected during the walk and reused for the summary.

## Behaviour

This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.

- Nothing here needs a third party package.
- A directory that cannot be read still appears in the output.

## Notes

This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.
