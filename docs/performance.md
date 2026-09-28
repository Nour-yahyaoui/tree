# Performance

Errors are reported once and do not stop the walk.

## Details

The counters are collected during the walk and reused for the summary.
This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
The public API is one function and two dataclasses.

## Usage

Errors are reported once and do not stop the walk.
Nothing here needs a third party package.

- A directory that cannot be read still appears in the output.
- A link that would loop is marked instead of followed.
