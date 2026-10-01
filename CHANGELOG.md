# Changelog

This keeps the output stable between runs on the same tree.

## Caveats

Symlinks are reported with their target.
The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.

## Design

The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.
The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

## Extensions

Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.

- This keeps the output stable between runs on the same tree.
- Everything else works on the tree it returns.

## Overview

Sizes are taken from the directory entry when the platform allows it.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
