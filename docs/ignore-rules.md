# Ignore Rules

A link that would loop is marked instead of followed.

## Caveats

The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.

## Design

This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.

- A directory that cannot be read still appears in the output.
- The exit code is one when anything failed.

## Extensions

The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.
The JSON document carries a version so consumers can check it.

## Overview

The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.
The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
