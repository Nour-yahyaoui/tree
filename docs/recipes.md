# Recipes

Colour is decided in a single place so the rest stays testable.

## Extensions

Symlinks are reported with their target.
A link that would loop is marked instead of followed.
The exit code is one when anything failed.

## Overview

Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
Nothing here needs a third party package.
Colour is decided in a single place so the rest stays testable.

## Details

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.

- Symlinks are reported with their target.
- Sorting happens while the directory is read, not afterwards.

## Usage

Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
