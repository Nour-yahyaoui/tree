# Architecture

A directory that cannot be read still appears in the output.

## Overview

A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
The summary line describes what was printed, not what was found.
Keeping this small makes the behaviour easy to reason about.

## Details

Patterns are matched against the path relative to the root of the scan.
This keeps the output stable between runs on the same tree.

- The JSON document carries a version so consumers can check it.
- Errors are reported once and do not stop the walk.

## Usage

The counters are collected during the walk and reused for the summary.
The public API is one function and two dataclasses.
The walker is the only module that touches the filesystem.
