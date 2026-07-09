# Recipes

Everything else works on the tree it returns.

## Overview

The exit code is one when anything failed.
Keeping this small makes the behaviour easy to reason about.

- This keeps the output stable between runs on the same tree.
- Colour is decided in a single place so the rest stays testable.

## Details

The walker is the only module that touches the filesystem.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.

## Usage

A link that would loop is marked instead of followed.
The walker is the only module that touches the filesystem.
Errors are reported once and do not stop the walk.
The JSON document carries a version so consumers can check it.
