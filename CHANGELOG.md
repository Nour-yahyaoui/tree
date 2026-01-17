# Changelog

The public API is one function and two dataclasses.

## Design

Errors are reported once and do not stop the walk.
Nothing here needs a third party package.
Everything else works on the tree it returns.
A link that would loop is marked instead of followed.

## Extensions

The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.

- Everything else works on the tree it returns.
- The public API is one function and two dataclasses.

## Overview

Nothing here needs a third party package.
Patterns are matched against the path relative to the root of the scan.
The glyphs are chosen once, when the renderer is built.
