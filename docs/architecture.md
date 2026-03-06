# Architecture

The counters are collected during the walk and reused for the summary.

## Extensions

A link that would loop is marked instead of followed.
Symlinks are reported with their target.
This keeps the output stable between runs on the same tree.

## Overview

Colour is decided in a single place so the rest stays testable.
Symlinks are reported with their target.
Tests use temporary directories only.
Errors are reported once and do not stop the walk.

## Details

This keeps the output stable between runs on the same tree.
The counters are collected during the walk and reused for the summary.

- This keeps the output stable between runs on the same tree.
- The glyphs are chosen once, when the renderer is built.

## Usage

Everything else works on the tree it returns.
Sizes are taken from the directory entry when the platform allows it.
A directory that cannot be read still appears in the output.
