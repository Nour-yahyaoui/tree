# Architecture

Everything else works on the tree it returns.

## Design

The counters are collected during the walk and reused for the summary.
The glyphs are chosen once, when the renderer is built.
This keeps the output stable between runs on the same tree.

## Extensions

Keeping this small makes the behaviour easy to reason about.
Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.
A directory that cannot be read still appears in the output.

## Overview

The summary line describes what was printed, not what was found.
The exit code is one when anything failed.

- The walker is the only module that touches the filesystem.
- The counters are collected during the walk and reused for the summary.
