# treepy

The walker is the only module that touches the filesystem.

## Details

The walker is the only module that touches the filesystem.
The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.
Sorting happens while the directory is read, not afterwards.

## Usage

The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.

- A link that would loop is marked instead of followed.
- Sorting happens while the directory is read, not afterwards.
