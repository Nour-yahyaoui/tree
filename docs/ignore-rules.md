# Ignore Rules

Colour is decided in a single place so the rest stays testable.

## Overview

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.

- Tests use temporary directories only.
- The exit code is one when anything failed.

## Details

The public API is one function and two dataclasses.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.

## Usage

A directory that cannot be read still appears in the output.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
Nothing here needs a third party package.
