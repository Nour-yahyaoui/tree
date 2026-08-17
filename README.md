# treepy

The counters are collected during the walk and reused for the summary.

## Behaviour

The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.

## Notes

The counters are collected during the walk and reused for the summary.
The summary line describes what was printed, not what was found.

- Sorting happens while the directory is read, not afterwards.
- A directory that cannot be read still appears in the output.
