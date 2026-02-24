# Ignore Rules

The summary line describes what was printed, not what was found.

## Usage

The JSON document carries a version so consumers can check it.
A directory that cannot be read still appears in the output.

- Colour is decided in a single place so the rest stays testable.
- Tests use temporary directories only.

## Behaviour

The counters are collected during the walk and reused for the summary.
Tests use temporary directories only.
The summary line describes what was printed, not what was found.

## Notes

A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.
The counters are collected during the walk and reused for the summary.
A link that would loop is marked instead of followed.
