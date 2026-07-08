# Changelog

Keeping this small makes the behaviour easy to reason about.

## Extensions

A link that would loop is marked instead of followed.
The public API is one function and two dataclasses.
Nothing here needs a third party package.
This keeps the output stable between runs on the same tree.

## Overview

The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.

- Everything else works on the tree it returns.
- Sizes are taken from the directory entry when the platform allows it.
