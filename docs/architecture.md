# Architecture

The counters are collected during the walk and reused for the summary.

## Behaviour

Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.

## Notes

Tests use temporary directories only.
The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.
Errors are reported once and do not stop the walk.
