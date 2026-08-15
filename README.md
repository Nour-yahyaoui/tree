# treepy

Errors are reported once and do not stop the walk.

## Behaviour

The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.

- Symlinks are reported with their target.
- The counters are collected during the walk and reused for the summary.

## Notes

The counters are collected during the walk and reused for the summary.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.
