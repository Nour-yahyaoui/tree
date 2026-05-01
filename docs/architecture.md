# Architecture

The walker is the only module that touches the filesystem.

## Extensions

The walker is the only module that touches the filesystem.
Nothing here needs a third party package.

- The glyphs are chosen once, when the renderer is built.
- Sizes are taken from the directory entry when the platform allows it.

## Overview

A link that would loop is marked instead of followed.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
