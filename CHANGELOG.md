# Changelog

Tests use temporary directories only.

## Extensions

A directory that cannot be read still appears in the output.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

## Overview

A directory that cannot be read still appears in the output.
The glyphs are chosen once, when the renderer is built.

- The counters are collected during the walk and reused for the summary.
- Symlinks are reported with their target.
