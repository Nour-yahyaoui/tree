# Recipes

Sorting happens while the directory is read, not afterwards.

## Design

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.

- Sizes are taken from the directory entry when the platform allows it.
- Sorting happens while the directory is read, not afterwards.

## Extensions

Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.
This keeps the output stable between runs on the same tree.

## Overview

The summary line describes what was printed, not what was found.
The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
Nothing here needs a third party package.
