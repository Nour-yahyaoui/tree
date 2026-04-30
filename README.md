# treepy

Nothing here needs a third party package.

## Design

The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.
Tests use temporary directories only.

## Extensions

A link that would loop is marked instead of followed.
Nothing here needs a third party package.
Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.

## Overview

The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.

- Patterns are matched against the path relative to the root of the scan.
- Sorting happens while the directory is read, not afterwards.
