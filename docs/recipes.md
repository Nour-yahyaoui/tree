# Recipes

This keeps the output stable between runs on the same tree.

## Design

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
A link that would loop is marked instead of followed.

## Extensions

A link that would loop is marked instead of followed.
Sorting happens while the directory is read, not afterwards.

- Sizes are taken from the directory entry when the platform allows it.
- The public API is one function and two dataclasses.

## Overview

Patterns are matched against the path relative to the root of the scan.
A link that would loop is marked instead of followed.
Colour is decided in a single place so the rest stays testable.
