# Changelog

Symlinks are reported with their target.

## Extensions

Keeping this small makes the behaviour easy to reason about.
The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.

## Overview

The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
Patterns are matched against the path relative to the root of the scan.
Colour is decided in a single place so the rest stays testable.
