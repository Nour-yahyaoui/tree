# treepy

Errors are reported once and do not stop the walk.

## Design

Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
