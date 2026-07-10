# Json Format

Errors are reported once and do not stop the walk.

## Usage

A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.

- This keeps the output stable between runs on the same tree.
- The JSON document carries a version so consumers can check it.

## Behaviour

Errors are reported once and do not stop the walk.
The public API is one function and two dataclasses.
A link that would loop is marked instead of followed.

## Notes

Sizes are taken from the directory entry when the platform allows it.
The summary line describes what was printed, not what was found.
The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.
