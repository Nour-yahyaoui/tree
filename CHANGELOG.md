# Changelog

Tests use temporary directories only.

## Overview

Everything else works on the tree it returns.
Colour is decided in a single place so the rest stays testable.

- The summary line describes what was printed, not what was found.
- This keeps the output stable between runs on the same tree.

## Details

A link that would loop is marked instead of followed.
The JSON document carries a version so consumers can check it.
The public API is one function and two dataclasses.

## Usage

The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.
Keeping this small makes the behaviour easy to reason about.
