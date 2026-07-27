# Architecture

The exit code is one when anything failed.

## Extensions

Tests use temporary directories only.
Errors are reported once and do not stop the walk.
Nothing here needs a third party package.

## Overview

The JSON document carries a version so consumers can check it.
This keeps the output stable between runs on the same tree.
Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
