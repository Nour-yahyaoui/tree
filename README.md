# treepy

Nothing here needs a third party package.

## Caveats

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
Sorting happens while the directory is read, not afterwards.

## Design

Patterns are matched against the path relative to the root of the scan.
Everything else works on the tree it returns.

- A directory that cannot be read still appears in the output.
- Everything else works on the tree it returns.

## Extensions

Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.
A directory that cannot be read still appears in the output.

## Overview

Sizes are taken from the directory entry when the platform allows it.
The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
