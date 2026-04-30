# treepy

The summary line describes what was printed, not what was found.

## Details

The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.
Everything else works on the tree it returns.

## Usage

The exit code is one when anything failed.
The walker is the only module that touches the filesystem.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.
