# Architecture

Errors are reported once and do not stop the walk.

## Design

Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.
The counters are collected during the walk and reused for the summary.

## Extensions

The summary line describes what was printed, not what was found.
Colour is decided in a single place so the rest stays testable.
The counters are collected during the walk and reused for the summary.
Patterns are matched against the path relative to the root of the scan.

## Overview

Sizes are taken from the directory entry when the platform allows it.
Colour is decided in a single place so the rest stays testable.

- The public API is one function and two dataclasses.
- Errors are reported once and do not stop the walk.
