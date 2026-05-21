# Architecture

A directory that cannot be read still appears in the output.

## Details

The exit code is one when anything failed.
The public API is one function and two dataclasses.
This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.

## Usage

Errors are reported once and do not stop the walk.
Symlinks are reported with their target.

- Sizes are taken from the directory entry when the platform allows it.
- The counters are collected during the walk and reused for the summary.
