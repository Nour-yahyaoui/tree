# Ignore Rules

A link that would loop is marked instead of followed.

## Overview

This keeps the output stable between runs on the same tree.
The JSON document carries a version so consumers can check it.

- Keeping this small makes the behaviour easy to reason about.
- A link that would loop is marked instead of followed.

## Details

A link that would loop is marked instead of followed.
Symlinks are reported with their target.
The counters are collected during the walk and reused for the summary.

## Usage

Everything else works on the tree it returns.
The walker is the only module that touches the filesystem.
The summary line describes what was printed, not what was found.
The exit code is one when anything failed.
