# Ignore Rules

Everything else works on the tree it returns.

## Caveats

A link that would loop is marked instead of followed.
Patterns are matched against the path relative to the root of the scan.

- This keeps the output stable between runs on the same tree.
- The JSON document carries a version so consumers can check it.

## Design

The public API is one function and two dataclasses.
Symlinks are reported with their target.
Nothing here needs a third party package.

## Extensions

The counters are collected during the walk and reused for the summary.
The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.

## Overview

This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.

- A directory that cannot be read still appears in the output.
- A link that would loop is marked instead of followed.
