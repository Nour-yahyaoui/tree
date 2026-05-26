# Architecture

Symlinks are reported with their target.

## Caveats

The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

## Design

Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.
