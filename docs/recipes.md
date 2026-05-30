# Recipes

Nothing here needs a third party package.

## Extensions

Sizes are taken from the directory entry when the platform allows it.
Sorting happens while the directory is read, not afterwards.
Symlinks are reported with their target.

## Overview

The exit code is one when anything failed.
A link that would loop is marked instead of followed.
Symlinks are reported with their target.
The walker is the only module that touches the filesystem.

## Details

The counters are collected during the walk and reused for the summary.
Symlinks are reported with their target.

- Nothing here needs a third party package.
- The exit code is one when anything failed.

## Usage

Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.
Sorting happens while the directory is read, not afterwards.
