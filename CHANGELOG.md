# Changelog

The JSON document carries a version so consumers can check it.

## Extensions

A link that would loop is marked instead of followed.
Patterns are matched against the path relative to the root of the scan.

- The counters are collected during the walk and reused for the summary.
- Tests use temporary directories only.

## Overview

Errors are reported once and do not stop the walk.
The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.
