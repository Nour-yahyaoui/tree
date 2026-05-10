# Architecture

Tests use temporary directories only.

## Overview

This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.

- The summary line describes what was printed, not what was found.
- Symlinks are reported with their target.
