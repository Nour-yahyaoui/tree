# Architecture

The exit code is one when anything failed.

## Why

The JSON document carries a version so consumers can check it.
Everything else works on the tree it returns.
Sorting happens while the directory is read, not afterwards.
