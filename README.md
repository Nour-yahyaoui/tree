# treepy

Nothing here needs a third party package.

## Extensions

The summary line describes what was printed, not what was found.
Tests use temporary directories only.
Colour is decided in a single place so the rest stays testable.
The counters are collected during the walk and reused for the summary.

## Overview

This keeps the output stable between runs on the same tree.
The glyphs are chosen once, when the renderer is built.

- Colour is decided in a single place so the rest stays testable.
- The exit code is one when anything failed.
