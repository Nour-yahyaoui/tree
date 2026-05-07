# Architecture

Tests use temporary directories only.

## Design

The JSON document carries a version so consumers can check it.
Tests use temporary directories only.

- Symlinks are reported with their target.
- A directory that cannot be read still appears in the output.

## Extensions

Tests use temporary directories only.
Sorting happens while the directory is read, not afterwards.
A directory that cannot be read still appears in the output.

## Overview

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.
The counters are collected during the walk and reused for the summary.
