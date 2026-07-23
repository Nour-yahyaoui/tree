# Recipes

The summary line describes what was printed, not what was found.

## Design

Errors are reported once and do not stop the walk.
Colour is decided in a single place so the rest stays testable.

- The counters are collected during the walk and reused for the summary.
- The public API is one function and two dataclasses.

## Extensions

The exit code is one when anything failed.
The JSON document carries a version so consumers can check it.
Nothing here needs a third party package.

## Overview

The summary line describes what was printed, not what was found.
A link that would loop is marked instead of followed.
Errors are reported once and do not stop the walk.
A directory that cannot be read still appears in the output.
