# Recipes

This keeps the output stable between runs on the same tree.

## Design

Patterns are matched against the path relative to the root of the scan.
Nothing here needs a third party package.
Sorting happens while the directory is read, not afterwards.
Colour is decided in a single place so the rest stays testable.

## Extensions

The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.

- The walker is the only module that touches the filesystem.
- A directory that cannot be read still appears in the output.

## Overview

This keeps the output stable between runs on the same tree.
The walker is the only module that touches the filesystem.
A directory that cannot be read still appears in the output.
