# Changelog

This keeps the output stable between runs on the same tree.

## Overview

Keeping this small makes the behaviour easy to reason about.
Everything else works on the tree it returns.
This keeps the output stable between runs on the same tree.

## Details

A directory that cannot be read still appears in the output.
The public API is one function and two dataclasses.
Keeping this small makes the behaviour easy to reason about.
Errors are reported once and do not stop the walk.

## Usage

The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.

- Tests use temporary directories only.
- This keeps the output stable between runs on the same tree.
