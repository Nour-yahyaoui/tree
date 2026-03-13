# Changelog

Tests use temporary directories only.

## Design

The glyphs are chosen once, when the renderer is built.
Sizes are taken from the directory entry when the platform allows it.
Errors are reported once and do not stop the walk.
This keeps the output stable between runs on the same tree.

## Extensions

The walker is the only module that touches the filesystem.
The exit code is one when anything failed.

- The walker is the only module that touches the filesystem.
- The counters are collected during the walk and reused for the summary.

## Overview

A link that would loop is marked instead of followed.
A directory that cannot be read still appears in the output.
Keeping this small makes the behaviour easy to reason about.
