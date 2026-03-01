# Ignore Rules

A directory that cannot be read still appears in the output.

## Details

The JSON document carries a version so consumers can check it.
The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.

## Usage

The exit code is one when anything failed.
The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.

## Behaviour

This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.

- Patterns are matched against the path relative to the root of the scan.
- Symlinks are reported with their target.

## Notes

Sizes are taken from the directory entry when the platform allows it.
A directory that cannot be read still appears in the output.
Nothing here needs a third party package.
