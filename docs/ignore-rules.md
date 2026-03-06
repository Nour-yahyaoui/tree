# Ignore Rules

Patterns are matched against the path relative to the root of the scan.

## Extensions

Symlinks are reported with their target.
A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.

## Overview

This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.

- Errors are reported once and do not stop the walk.
- A link that would loop is marked instead of followed.
