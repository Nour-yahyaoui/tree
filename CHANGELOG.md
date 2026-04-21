# Changelog

Nothing here needs a third party package.

## Extensions

A directory that cannot be read still appears in the output.
The JSON document carries a version so consumers can check it.
Patterns are matched against the path relative to the root of the scan.
Sorting happens while the directory is read, not afterwards.

## Overview

Sorting happens while the directory is read, not afterwards.
Patterns are matched against the path relative to the root of the scan.

- Colour is decided in a single place so the rest stays testable.
- Sizes are taken from the directory entry when the platform allows it.
