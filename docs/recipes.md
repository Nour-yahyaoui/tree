# Recipes

The walker is the only module that touches the filesystem.

## Overview

The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.

## Details

A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.

- Keeping this small makes the behaviour easy to reason about.
- Keeping this small makes the behaviour easy to reason about.

## Usage

Colour is decided in a single place so the rest stays testable.
Keeping this small makes the behaviour easy to reason about.
The exit code is one when anything failed.
