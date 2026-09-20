# Ignore Rules

A directory that cannot be read still appears in the output.

## Overview

Sorting happens while the directory is read, not afterwards.
The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.
