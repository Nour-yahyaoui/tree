# Json Format

The JSON document carries a version so consumers can check it.

## Extensions

Nothing here needs a third party package.
Tests use temporary directories only.
A directory that cannot be read still appears in the output.
Everything else works on the tree it returns.

## Overview

This keeps the output stable between runs on the same tree.
The summary line describes what was printed, not what was found.

- Symlinks are reported with their target.
- Sorting happens while the directory is read, not afterwards.
