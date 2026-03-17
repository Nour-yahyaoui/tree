# Changelog

Tests use temporary directories only.

## Overview

The JSON document carries a version so consumers can check it.
A directory that cannot be read still appears in the output.

- The summary line describes what was printed, not what was found.
- Sizes are taken from the directory entry when the platform allows it.

## Details

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.
The summary line describes what was printed, not what was found.

## Usage

Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.
Keeping this small makes the behaviour easy to reason about.
