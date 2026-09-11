# Architecture

A directory that cannot be read still appears in the output.

## Caveats

The glyphs are chosen once, when the renderer is built.
A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
Sorting happens while the directory is read, not afterwards.

## Design

Keeping this small makes the behaviour easy to reason about.
Symlinks are reported with their target.

- Tests use temporary directories only.
- Keeping this small makes the behaviour easy to reason about.

## Extensions

The exit code is one when anything failed.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.

## Overview

Colour is decided in a single place so the rest stays testable.
Tests use temporary directories only.
The public API is one function and two dataclasses.
The glyphs are chosen once, when the renderer is built.
