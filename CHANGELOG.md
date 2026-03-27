# Changelog

The summary line describes what was printed, not what was found.

## Details

The walker is the only module that touches the filesystem.
Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.

## Usage

The counters are collected during the walk and reused for the summary.
Tests use temporary directories only.
The JSON document carries a version so consumers can check it.
Sorting happens while the directory is read, not afterwards.
