# treepy

Patterns are matched against the path relative to the root of the scan.

## Extensions

This keeps the output stable between runs on the same tree.
The exit code is one when anything failed.
Nothing here needs a third party package.

## Overview

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.

## Details

Colour is decided in a single place so the rest stays testable.
Errors are reported once and do not stop the walk.

- Patterns are matched against the path relative to the root of the scan.
- The walker is the only module that touches the filesystem.

## Usage

Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.
