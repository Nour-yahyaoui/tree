# treepy

A link that would loop is marked instead of followed.

## Extensions

Keeping this small makes the behaviour easy to reason about.
The public API is one function and two dataclasses.

- A directory that cannot be read still appears in the output.
- Everything else works on the tree it returns.

## Overview

Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.
The exit code is one when anything failed.
