# Changelog

A directory that cannot be read still appears in the output.

## Overview

Sizes are taken from the directory entry when the platform allows it.
Everything else works on the tree it returns.
The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.

## Details

Nothing here needs a third party package.
The glyphs are chosen once, when the renderer is built.

- The exit code is one when anything failed.
- The walker is the only module that touches the filesystem.

## Usage

A directory that cannot be read still appears in the output.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
