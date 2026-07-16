# treepy

Symlinks are reported with their target.

## Extensions

Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.
The glyphs are chosen once, when the renderer is built.

## Overview

The counters are collected during the walk and reused for the summary.
Everything else works on the tree it returns.
The exit code is one when anything failed.
The glyphs are chosen once, when the renderer is built.
