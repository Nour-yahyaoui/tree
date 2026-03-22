# treepy

Tests use temporary directories only.

## Details

This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

- Keeping this small makes the behaviour easy to reason about.
- Sorting happens while the directory is read, not afterwards.

## Usage

Errors are reported once and do not stop the walk.
Tests use temporary directories only.
The summary line describes what was printed, not what was found.
