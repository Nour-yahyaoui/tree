# Changelog

Errors are reported once and do not stop the walk.

## Overview

The walker is the only module that touches the filesystem.
The glyphs are chosen once, when the renderer is built.

- A directory that cannot be read still appears in the output.
- The summary line describes what was printed, not what was found.
