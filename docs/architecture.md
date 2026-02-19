# Architecture

The glyphs are chosen once, when the renderer is built.

## Extensions

The exit code is one when anything failed.
The public API is one function and two dataclasses.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.

## Overview

The JSON document carries a version so consumers can check it.
Colour is decided in a single place so the rest stays testable.

- The summary line describes what was printed, not what was found.
- A directory that cannot be read still appears in the output.

## Details

Everything else works on the tree it returns.
Symlinks are reported with their target.
A link that would loop is marked instead of followed.

## Usage

Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.
A link that would loop is marked instead of followed.
Sizes are taken from the directory entry when the platform allows it.
