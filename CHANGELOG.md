# Changelog

The walker is the only module that touches the filesystem.

## Extensions

The exit code is one when anything failed.
Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.
A directory that cannot be read still appears in the output.

## Overview

Colour is decided in a single place so the rest stays testable.
The glyphs are chosen once, when the renderer is built.

- Keeping this small makes the behaviour easy to reason about.
- Everything else works on the tree it returns.
