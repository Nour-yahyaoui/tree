# Changelog

The walker is the only module that touches the filesystem.

## Design

The glyphs are chosen once, when the renderer is built.
Colour is decided in a single place so the rest stays testable.
Nothing here needs a third party package.
A link that would loop is marked instead of followed.

## Extensions

Patterns are matched against the path relative to the root of the scan.
Errors are reported once and do not stop the walk.

- Errors are reported once and do not stop the walk.
- Nothing here needs a third party package.

## Overview

The public API is one function and two dataclasses.
Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.
