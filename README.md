# treepy

The public API is one function and two dataclasses.

## Overview

Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.

- Sizes are taken from the directory entry when the platform allows it.
- This keeps the output stable between runs on the same tree.

## Details

Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.

## Usage

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.
This keeps the output stable between runs on the same tree.
Keeping this small makes the behaviour easy to reason about.
