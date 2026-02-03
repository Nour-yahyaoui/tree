# Changelog

Tests use temporary directories only.

## Design

Tests use temporary directories only.
Everything else works on the tree it returns.
Symlinks are reported with their target.
Errors are reported once and do not stop the walk.

## Extensions

The counters are collected during the walk and reused for the summary.
Sizes are taken from the directory entry when the platform allows it.

- A link that would loop is marked instead of followed.
- Errors are reported once and do not stop the walk.

## Overview

The walker is the only module that touches the filesystem.
Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
