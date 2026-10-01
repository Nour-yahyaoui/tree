# Json Format

This keeps the output stable between runs on the same tree.

## Extensions

The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.

- The summary line describes what was printed, not what was found.
- Symlinks are reported with their target.

## Overview

Errors are reported once and do not stop the walk.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.
