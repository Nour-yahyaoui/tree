# treepy

The glyphs are chosen once, when the renderer is built.

## Overview

The public API is one function and two dataclasses.
Patterns are matched against the path relative to the root of the scan.

- Errors are reported once and do not stop the walk.
- The exit code is one when anything failed.
