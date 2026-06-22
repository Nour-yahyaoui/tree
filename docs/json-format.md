# Json Format

Errors are reported once and do not stop the walk.

## Behaviour

Sizes are taken from the directory entry when the platform allows it.
The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.

## Notes

Tests use temporary directories only.
Nothing here needs a third party package.

- A directory that cannot be read still appears in the output.
- Everything else works on the tree it returns.
