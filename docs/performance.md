# Performance

This keeps the output stable between runs on the same tree.

## Extensions

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.
The walker is the only module that touches the filesystem.

## Overview

The counters are collected during the walk and reused for the summary.
Sorting happens while the directory is read, not afterwards.
A directory that cannot be read still appears in the output.
A link that would loop is marked instead of followed.

## Details

The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.

- The summary line describes what was printed, not what was found.
- Errors are reported once and do not stop the walk.

## Usage

Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.
