# Architecture

Patterns are matched against the path relative to the root of the scan.

## Details

Tests use temporary directories only.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

## Usage

Sizes are taken from the directory entry when the platform allows it.
The exit code is one when anything failed.

- The walker is the only module that touches the filesystem.
- Sorting happens while the directory is read, not afterwards.
