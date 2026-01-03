# Recipes

Everything else works on the tree it returns.

## Overview

Patterns are matched against the path relative to the root of the scan.
The JSON document carries a version so consumers can check it.

- Sizes are taken from the directory entry when the platform allows it.
- The public API is one function and two dataclasses.

## Details

Keeping this small makes the behaviour easy to reason about.
A link that would loop is marked instead of followed.
Colour is decided in a single place so the rest stays testable.

## Usage

This keeps the output stable between runs on the same tree.
The public API is one function and two dataclasses.
Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.
