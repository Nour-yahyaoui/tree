# Performance

The counters are collected during the walk and reused for the summary.

## Notes

Keeping this small makes the behaviour easy to reason about.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
