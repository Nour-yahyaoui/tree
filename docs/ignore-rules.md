# Ignore Rules

The walker is the only module that touches the filesystem.

## Overview

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.

- The JSON document carries a version so consumers can check it.
- Symlinks are reported with their target.
