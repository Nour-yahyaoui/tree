# Changelog

The counters are collected during the walk and reused for the summary.

## Extensions

Everything else works on the tree it returns.
The summary line describes what was printed, not what was found.

- Colour is decided in a single place so the rest stays testable.
- The glyphs are chosen once, when the renderer is built.

## Overview

The exit code is one when anything failed.
The summary line describes what was printed, not what was found.
Everything else works on the tree it returns.
