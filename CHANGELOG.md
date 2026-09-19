# Changelog

The counters are collected during the walk and reused for the summary.

## Design

Keeping this small makes the behaviour easy to reason about.
A directory that cannot be read still appears in the output.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.
