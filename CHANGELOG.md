# Changelog

Colour is decided in a single place so the rest stays testable.

## Notes

Patterns are matched against the path relative to the root of the scan.
The counters are collected during the walk and reused for the summary.
Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.
