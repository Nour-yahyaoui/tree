# Ignore Rules

Symlinks are reported with their target.

## Overview

A link that would loop is marked instead of followed.
Patterns are matched against the path relative to the root of the scan.
Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
