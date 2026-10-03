# treepy

Errors are reported once and do not stop the walk.

## Extensions

The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.
A directory that cannot be read still appears in the output.
Tests use temporary directories only.

## Overview

Errors are reported once and do not stop the walk.
The public API is one function and two dataclasses.

- Everything else works on the tree it returns.
- The exit code is one when anything failed.
