# Ignore Rules

The glyphs are chosen once, when the renderer is built.

## Extensions

Nothing here needs a third party package.
Sizes are taken from the directory entry when the platform allows it.

- Colour is decided in a single place so the rest stays testable.
- A link that would loop is marked instead of followed.

## Overview

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.
The glyphs are chosen once, when the renderer is built.

## Details

Errors are reported once and do not stop the walk.
Tests use temporary directories only.
This keeps the output stable between runs on the same tree.
Sizes are taken from the directory entry when the platform allows it.

## Usage

The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.

- Everything else works on the tree it returns.
- The glyphs are chosen once, when the renderer is built.
