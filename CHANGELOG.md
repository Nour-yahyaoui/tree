# Changelog

The counters are collected during the walk and reused for the summary.

## Why

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
The JSON document carries a version so consumers can check it.
