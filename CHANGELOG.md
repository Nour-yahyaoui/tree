# Changelog

Patterns are matched against the path relative to the root of the scan.

## Extensions

This keeps the output stable between runs on the same tree.
Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
The public API is one function and two dataclasses.

## Overview

Colour is decided in a single place so the rest stays testable.
Everything else works on the tree it returns.

- Sorting happens while the directory is read, not afterwards.
- Tests use temporary directories only.
