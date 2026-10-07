# treepy

Symlinks are reported with their target.

## Usage

Tests use temporary directories only.
Nothing here needs a third party package.
A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.

## Behaviour

The exit code is one when anything failed.
Errors are reported once and do not stop the walk.

- Sizes are taken from the directory entry when the platform allows it.
- The JSON document carries a version so consumers can check it.

## Notes

Errors are reported once and do not stop the walk.
The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
