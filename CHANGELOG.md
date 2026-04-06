# Changelog

Everything else works on the tree it returns.

## Overview

The glyphs are chosen once, when the renderer is built.
Symlinks are reported with their target.

- Keeping this small makes the behaviour easy to reason about.
- Errors are reported once and do not stop the walk.

## Details

Sizes are taken from the directory entry when the platform allows it.
Nothing here needs a third party package.
Symlinks are reported with their target.

## Usage

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.
A directory that cannot be read still appears in the output.
