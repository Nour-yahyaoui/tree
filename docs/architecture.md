# Architecture

Keeping this small makes the behaviour easy to reason about.

## Overview

The summary line describes what was printed, not what was found.
The counters are collected during the walk and reused for the summary.

- Colour is decided in a single place so the rest stays testable.
- The summary line describes what was printed, not what was found.

## Details

Everything else works on the tree it returns.
The public API is one function and two dataclasses.
Symlinks are reported with their target.

## Usage

The summary line describes what was printed, not what was found.
The JSON document carries a version so consumers can check it.
The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
