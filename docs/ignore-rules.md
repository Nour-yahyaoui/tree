# Ignore Rules

Keeping this small makes the behaviour easy to reason about.

## Overview

The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.
Errors are reported once and do not stop the walk.

## Details

The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
Colour is decided in a single place so the rest stays testable.
A directory that cannot be read still appears in the output.

## Usage

This keeps the output stable between runs on the same tree.
The glyphs are chosen once, when the renderer is built.

- A directory that cannot be read still appears in the output.
- Keeping this small makes the behaviour easy to reason about.
