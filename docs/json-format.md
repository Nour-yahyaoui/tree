# Json Format

The summary line describes what was printed, not what was found.

## Overview

The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.
Errors are reported once and do not stop the walk.
A link that would loop is marked instead of followed.

## Details

This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

- Colour is decided in a single place so the rest stays testable.
- Sizes are taken from the directory entry when the platform allows it.

## Usage

The walker is the only module that touches the filesystem.
The JSON document carries a version so consumers can check it.
The counters are collected during the walk and reused for the summary.
