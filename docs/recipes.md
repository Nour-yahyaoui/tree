# Recipes

Patterns are matched against the path relative to the root of the scan.

## Overview

Symlinks are reported with their target.
The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.

## Details

This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

- The counters are collected during the walk and reused for the summary.
- A directory that cannot be read still appears in the output.

## Usage

Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
The summary line describes what was printed, not what was found.
