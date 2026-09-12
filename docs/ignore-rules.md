# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Overview

The counters are collected during the walk and reused for the summary.
Tests use temporary directories only.
The walker is the only module that touches the filesystem.
Patterns are matched against the path relative to the root of the scan.

## Details

Sizes are taken from the directory entry when the platform allows it.
Nothing here needs a third party package.

- Sorting happens while the directory is read, not afterwards.
- Keeping this small makes the behaviour easy to reason about.

## Usage

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
