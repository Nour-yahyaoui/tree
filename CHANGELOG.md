# Changelog

Patterns are matched against the path relative to the root of the scan.

## Design

Sorting happens while the directory is read, not afterwards.
Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Tests use temporary directories only.

## Extensions

The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.

- The public API is one function and two dataclasses.
- Sorting happens while the directory is read, not afterwards.

## Overview

Errors are reported once and do not stop the walk.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
