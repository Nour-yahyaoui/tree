# Changelog

A directory that cannot be read still appears in the output.

## Extensions

A link that would loop is marked instead of followed.
Sorting happens while the directory is read, not afterwards.
This keeps the output stable between runs on the same tree.

## Overview

Tests use temporary directories only.
Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.
A directory that cannot be read still appears in the output.

## Details

Symlinks are reported with their target.
Tests use temporary directories only.

- Patterns are matched against the path relative to the root of the scan.
- Errors are reported once and do not stop the walk.

## Usage

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.
