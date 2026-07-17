# Json Format

Colour is decided in a single place so the rest stays testable.

## Overview

Sorting happens while the directory is read, not afterwards.
Keeping this small makes the behaviour easy to reason about.

- A link that would loop is marked instead of followed.
- The public API is one function and two dataclasses.
