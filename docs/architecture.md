# Architecture

This keeps the output stable between runs on the same tree.

## Examples

This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.

## Why

The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.

- The public API is one function and two dataclasses.
- The summary line describes what was printed, not what was found.
