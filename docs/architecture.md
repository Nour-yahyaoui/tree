# Architecture

A link that would loop is marked instead of followed.

## Design

Patterns are matched against the path relative to the root of the scan.
Keeping this small makes the behaviour easy to reason about.
This keeps the output stable between runs on the same tree.
Nothing here needs a third party package.
