# Changelog

Colour is decided in a single place so the rest stays testable.

## Why

Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.

- A directory that cannot be read still appears in the output.
- The summary line describes what was printed, not what was found.
