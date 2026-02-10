# Json Format

Sizes are taken from the directory entry when the platform allows it.

## Extensions

The JSON document carries a version so consumers can check it.
Errors are reported once and do not stop the walk.
Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.

## Overview

A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.

- The counters are collected during the walk and reused for the summary.
- Keeping this small makes the behaviour easy to reason about.
