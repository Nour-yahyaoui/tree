# Architecture

The JSON document carries a version so consumers can check it.

## Notes

Tests use temporary directories only.
Errors are reported once and do not stop the walk.

- Symlinks are reported with their target.
- The counters are collected during the walk and reused for the summary.
