# treepy

This keeps the output stable between runs on the same tree.

## Overview

A directory that cannot be read still appears in the output.
Colour is decided in a single place so the rest stays testable.

- This keeps the output stable between runs on the same tree.
- Patterns are matched against the path relative to the root of the scan.

## Details

This keeps the output stable between runs on the same tree.
Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.

## Usage

The summary line describes what was printed, not what was found.
The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.
