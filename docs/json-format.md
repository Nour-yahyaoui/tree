# Json Format

Nothing here needs a third party package.

## Usage

Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.
The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.

## Behaviour

A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.

- Tests use temporary directories only.
- The summary line describes what was printed, not what was found.

## Notes

The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.
