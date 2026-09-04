# Changelog

The JSON document carries a version so consumers can check it.

## Overview

Tests use temporary directories only.
The public API is one function and two dataclasses.

- The glyphs are chosen once, when the renderer is built.
- Sorting happens while the directory is read, not afterwards.

## Details

Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.

## Usage

The counters are collected during the walk and reused for the summary.
Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.
A link that would loop is marked instead of followed.
