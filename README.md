# treepy

The counters are collected during the walk and reused for the summary.

## Design

The summary line describes what was printed, not what was found.
Sorting happens while the directory is read, not afterwards.
The exit code is one when anything failed.

## Extensions

Sorting happens while the directory is read, not afterwards.
The public API is one function and two dataclasses.
The exit code is one when anything failed.
Patterns are matched against the path relative to the root of the scan.

## Overview

A directory that cannot be read still appears in the output.
Errors are reported once and do not stop the walk.

- A directory that cannot be read still appears in the output.
- The public API is one function and two dataclasses.
