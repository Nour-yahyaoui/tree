# Ignore Rules

The exit code is one when anything failed.

## Extensions

Sorting happens while the directory is read, not afterwards.
Errors are reported once and do not stop the walk.

- The walker is the only module that touches the filesystem.
- This keeps the output stable between runs on the same tree.

## Overview

The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.
