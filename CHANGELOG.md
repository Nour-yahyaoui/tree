# Changelog

The JSON document carries a version so consumers can check it.

## Extensions

Symlinks are reported with their target.
The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.

## Overview

The summary line describes what was printed, not what was found.
Sizes are taken from the directory entry when the platform allows it.
This keeps the output stable between runs on the same tree.
Colour is decided in a single place so the rest stays testable.
