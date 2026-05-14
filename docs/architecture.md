# Architecture

The summary line describes what was printed, not what was found.

## Details

Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
The counters are collected during the walk and reused for the summary.
Tests use temporary directories only.

## Usage

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

- The exit code is one when anything failed.
- Keeping this small makes the behaviour easy to reason about.
