# Ignore Rules

The walker is the only module that touches the filesystem.

## Caveats

The public API is one function and two dataclasses.
The counters are collected during the walk and reused for the summary.
Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.

## Design

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.

- The JSON document carries a version so consumers can check it.
- The JSON document carries a version so consumers can check it.

## Extensions

The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
Sizes are taken from the directory entry when the platform allows it.

## Overview

Sorting happens while the directory is read, not afterwards.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.
The JSON document carries a version so consumers can check it.
