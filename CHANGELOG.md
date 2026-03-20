# Changelog

Patterns are matched against the path relative to the root of the scan.

## Why

Keeping this small makes the behaviour easy to reason about.
A directory that cannot be read still appears in the output.
Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.
