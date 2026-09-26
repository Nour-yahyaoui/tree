# Architecture

Patterns are matched against the path relative to the root of the scan.

## Design

The public API is one function and two dataclasses.
A link that would loop is marked instead of followed.
Tests use temporary directories only.
