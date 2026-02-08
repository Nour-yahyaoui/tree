# Json Format

Errors are reported once and do not stop the walk.

## Overview

The counters are collected during the walk and reused for the summary.
Colour is decided in a single place so the rest stays testable.
The JSON document carries a version so consumers can check it.

## Details

Colour is decided in a single place so the rest stays testable.
Sorting happens while the directory is read, not afterwards.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.

## Usage

Sizes are taken from the directory entry when the platform allows it.
The public API is one function and two dataclasses.

- A link that would loop is marked instead of followed.
- The exit code is one when anything failed.
