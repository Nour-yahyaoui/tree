# Ignore Rules

Sorting happens while the directory is read, not afterwards.

## Overview

Everything else works on the tree it returns.
Sizes are taken from the directory entry when the platform allows it.
The exit code is one when anything failed.
Colour is decided in a single place so the rest stays testable.

## Details

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.

- Symlinks are reported with their target.
- The exit code is one when anything failed.

## Usage

Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.
Nothing here needs a third party package.
