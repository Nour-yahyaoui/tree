# Changelog

The JSON document carries a version so consumers can check it.

## Examples

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
Errors are reported once and do not stop the walk.
The summary line describes what was printed, not what was found.

## Why

Sorting happens while the directory is read, not afterwards.
Errors are reported once and do not stop the walk.

- Nothing here needs a third party package.
- The summary line describes what was printed, not what was found.
