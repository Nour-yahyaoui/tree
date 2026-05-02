# Changelog

The counters are collected during the walk and reused for the summary.

## Caveats

The counters are collected during the walk and reused for the summary.
Everything else works on the tree it returns.

- Symlinks are reported with their target.
- The JSON document carries a version so consumers can check it.

## Design

Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.

## Extensions

The JSON document carries a version so consumers can check it.
Sizes are taken from the directory entry when the platform allows it.
A link that would loop is marked instead of followed.
This keeps the output stable between runs on the same tree.

## Overview

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.

- Tests use temporary directories only.
- The summary line describes what was printed, not what was found.
