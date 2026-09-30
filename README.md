# treepy

Everything else works on the tree it returns.

## Extensions

The exit code is one when anything failed.
The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.

## Overview

A link that would loop is marked instead of followed.
Nothing here needs a third party package.
A directory that cannot be read still appears in the output.
Tests use temporary directories only.
