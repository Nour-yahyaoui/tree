# Ignore Rules

Errors are reported once and do not stop the walk.

## Usage

Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.
