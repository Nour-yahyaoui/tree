# treepy

Sorting happens while the directory is read, not afterwards.

## Design

A link that would loop is marked instead of followed.
Everything else works on the tree it returns.
Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

## Extensions

Nothing here needs a third party package.
The JSON document carries a version so consumers can check it.

- Errors are reported once and do not stop the walk.
- Colour is decided in a single place so the rest stays testable.

## Overview

Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.
The exit code is one when anything failed.
