# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Usage

Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.

## Behaviour

A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.

## Notes

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.

- Errors are reported once and do not stop the walk.
- Tests use temporary directories only.
