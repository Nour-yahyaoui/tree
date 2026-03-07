# Architecture

The JSON document carries a version so consumers can check it.

## Overview

Sorting happens while the directory is read, not afterwards.
Tests use temporary directories only.

- Patterns are matched against the path relative to the root of the scan.
- The public API is one function and two dataclasses.

## Details

A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.
The JSON document carries a version so consumers can check it.

## Usage

Keeping this small makes the behaviour easy to reason about.
The walker is the only module that touches the filesystem.
Everything else works on the tree it returns.
The JSON document carries a version so consumers can check it.
