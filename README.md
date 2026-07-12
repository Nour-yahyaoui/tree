# treepy

Symlinks are reported with their target.

## Extensions

Everything else works on the tree it returns.
Nothing here needs a third party package.

- The walker is the only module that touches the filesystem.
- This keeps the output stable between runs on the same tree.

## Overview

The public API is one function and two dataclasses.
Errors are reported once and do not stop the walk.
Sizes are taken from the directory entry when the platform allows it.
