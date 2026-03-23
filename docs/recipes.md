# Recipes

The exit code is one when anything failed.

## Caveats

Patterns are matched against the path relative to the root of the scan.
A directory that cannot be read still appears in the output.

- The counters are collected during the walk and reused for the summary.
- Patterns are matched against the path relative to the root of the scan.

## Design

The glyphs are chosen once, when the renderer is built.
Nothing here needs a third party package.
The counters are collected during the walk and reused for the summary.

## Extensions

The walker is the only module that touches the filesystem.
A link that would loop is marked instead of followed.
The counters are collected during the walk and reused for the summary.
Nothing here needs a third party package.

## Overview

A link that would loop is marked instead of followed.
Everything else works on the tree it returns.

- Errors are reported once and do not stop the walk.
- Errors are reported once and do not stop the walk.
