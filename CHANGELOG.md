# Changelog

Colour is decided in a single place so the rest stays testable.

## Extensions

The JSON document carries a version so consumers can check it.
Symlinks are reported with their target.
Sizes are taken from the directory entry when the platform allows it.

## Overview

Symlinks are reported with their target.
Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.
A directory that cannot be read still appears in the output.

## Details

The public API is one function and two dataclasses.
Sorting happens while the directory is read, not afterwards.

- This keeps the output stable between runs on the same tree.
- The counters are collected during the walk and reused for the summary.

## Usage

A link that would loop is marked instead of followed.
Nothing here needs a third party package.
Errors are reported once and do not stop the walk.
