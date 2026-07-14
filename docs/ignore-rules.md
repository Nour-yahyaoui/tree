# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Overview

The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.

- Colour is decided in a single place so the rest stays testable.
- Tests use temporary directories only.

## Details

Sizes are taken from the directory entry when the platform allows it.
Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.

## Usage

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.
