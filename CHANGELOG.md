# Changelog

Errors are reported once and do not stop the walk.

## Extensions

Colour is decided in a single place so the rest stays testable.
The walker is the only module that touches the filesystem.

- Nothing here needs a third party package.
- Symlinks are reported with their target.

## Overview

Symlinks are reported with their target.
The glyphs are chosen once, when the renderer is built.
Nothing here needs a third party package.
