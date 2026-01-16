# Json Format

Patterns are matched against the path relative to the root of the scan.

## Overview

The public API is one function and two dataclasses.
The summary line describes what was printed, not what was found.

- Keeping this small makes the behaviour easy to reason about.
- Sorting happens while the directory is read, not afterwards.

## Details

The summary line describes what was printed, not what was found.
Tests use temporary directories only.
Sorting happens while the directory is read, not afterwards.

## Usage

Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.
