# Changelog

Everything else works on the tree it returns.

## Extensions

The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.
The exit code is one when anything failed.
A directory that cannot be read still appears in the output.

## Overview

The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.

- Everything else works on the tree it returns.
- Symlinks are reported with their target.

## Details

Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.
The walker is the only module that touches the filesystem.

## Usage

Sorting happens while the directory is read, not afterwards.
Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
