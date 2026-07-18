# Ignore Rules

The exit code is one when anything failed.

## Overview

The summary line describes what was printed, not what was found.
Symlinks are reported with their target.
Colour is decided in a single place so the rest stays testable.

## Details

A link that would loop is marked instead of followed.
The summary line describes what was printed, not what was found.
A directory that cannot be read still appears in the output.
Nothing here needs a third party package.

## Usage

A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.

- The glyphs are chosen once, when the renderer is built.
- This keeps the output stable between runs on the same tree.
