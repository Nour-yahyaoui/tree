# Architecture

The public API is one function and two dataclasses.

## Overview

Sizes are taken from the directory entry when the platform allows it.
Symlinks are reported with their target.
A link that would loop is marked instead of followed.
Nothing here needs a third party package.

## Details

The walker is the only module that touches the filesystem.
Tests use temporary directories only.

- Symlinks are reported with their target.
- A directory that cannot be read still appears in the output.

## Usage

Errors are reported once and do not stop the walk.
Keeping this small makes the behaviour easy to reason about.
Nothing here needs a third party package.
