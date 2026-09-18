# Performance

Tests use temporary directories only.

## Overview

Patterns are matched against the path relative to the root of the scan.
Sorting happens while the directory is read, not afterwards.

- The counters are collected during the walk and reused for the summary.
- Errors are reported once and do not stop the walk.
