# Json Format

A link that would loop is marked instead of followed.

## Why

Nothing here needs a third party package.
The exit code is one when anything failed.

- Sorting happens while the directory is read, not afterwards.
- The summary line describes what was printed, not what was found.

## Caveats

The summary line describes what was printed, not what was found.
The exit code is one when anything failed.
The walker is the only module that touches the filesystem.

## Design

A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
