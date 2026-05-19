# Architecture

This keeps the output stable between runs on the same tree.

## Design

The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.

- A directory that cannot be read still appears in the output.
- Symlinks are reported with their target.

## Extensions

This keeps the output stable between runs on the same tree.
Keeping this small makes the behaviour easy to reason about.
The glyphs are chosen once, when the renderer is built.

## Overview

The public API is one function and two dataclasses.
The glyphs are chosen once, when the renderer is built.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.
