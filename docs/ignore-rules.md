# Ignore Rules

Symlinks are reported with their target.

## Overview

The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.
Tests use temporary directories only.

## Details

The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
Symlinks are reported with their target.

## Usage

Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.

- The walker is the only module that touches the filesystem.
- A directory that cannot be read still appears in the output.
