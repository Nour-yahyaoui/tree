# treepy

The counters are collected during the walk and reused for the summary.

## Overview

Errors are reported once and do not stop the walk.
The glyphs are chosen once, when the renderer is built.
Sorting happens while the directory is read, not afterwards.

## Details

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
The glyphs are chosen once, when the renderer is built.
The counters are collected during the walk and reused for the summary.

## Usage

Keeping this small makes the behaviour easy to reason about.
Sizes are taken from the directory entry when the platform allows it.

- The JSON document carries a version so consumers can check it.
- Colour is decided in a single place so the rest stays testable.
