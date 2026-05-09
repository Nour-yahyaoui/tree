# Architecture

Keeping this small makes the behaviour easy to reason about.

## Notes

Sizes are taken from the directory entry when the platform allows it.
Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.
