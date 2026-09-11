# Recipes

Colour is decided in a single place so the rest stays testable.

## Notes

The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
Errors are reported once and do not stop the walk.
Tests use temporary directories only.
