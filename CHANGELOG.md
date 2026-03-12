# Changelog

Patterns are matched against the path relative to the root of the scan.

## Usage

Errors are reported once and do not stop the walk.
The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.

## Behaviour

The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.
The exit code is one when anything failed.
A link that would loop is marked instead of followed.

## Notes

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

- Patterns are matched against the path relative to the root of the scan.
- Nothing here needs a third party package.
