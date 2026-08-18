# treepy

Keeping this small makes the behaviour easy to reason about.

## Why

Nothing here needs a third party package.
The walker is the only module that touches the filesystem.
The counters are collected during the walk and reused for the summary.
Keeping this small makes the behaviour easy to reason about.
