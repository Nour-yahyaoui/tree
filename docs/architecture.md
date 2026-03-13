# Architecture

A directory that cannot be read still appears in the output.

## Extensions

This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.

- The walker is the only module that touches the filesystem.
- The public API is one function and two dataclasses.

## Overview

The summary line describes what was printed, not what was found.
This keeps the output stable between runs on the same tree.
Sorting happens while the directory is read, not afterwards.

## Details

The JSON document carries a version so consumers can check it.
The summary line describes what was printed, not what was found.
Tests use temporary directories only.
Colour is decided in a single place so the rest stays testable.

## Usage

Everything else works on the tree it returns.
Keeping this small makes the behaviour easy to reason about.

- A directory that cannot be read still appears in the output.
- The counters are collected during the walk and reused for the summary.
